#!/usr/bin/python
# -*- coding: utf-8 -*-

import calendar
import logging
import gc

from datetime import datetime
from flask import Flask, request, json
from flask.json import JSONEncoder
from flask_compress import Compress
from base64 import b64decode
from webhook.utils import get_args

from google.protobuf.json_format import MessageToJson
from webhook.protos.pogoprotos.networking.responses.fort_search_response_pb2 import FortSearchResponse
from webhook.protos.pogoprotos.networking.responses.encounter_response_pb2 import EncounterResponse
from webhook.protos.pogoprotos.networking.responses.get_map_objects_response_pb2 import GetMapObjectsResponse, _GETMAPOBJECTSRESPONSE_TIMEOFDAY
from webhook.protos.pogoprotos.networking.responses.gym_get_info_response_pb2 import GymGetInfoResponse
from webhook.protos.pogoprotos.networking.responses.fort_details_response_pb2 import FortDetailsResponse
from webhook.protos.pogoprotos.networking.responses.get_player_response_pb2 import GetPlayerResponse
from webhook.protos.pogoprotos.map.weather.display_weather_pb2 import _DISPLAYWEATHER_DISPLAYLEVEL
from webhook.protos.pogoprotos.map.weather.gameplay_weather_pb2 import _GAMEPLAYWEATHER_WEATHERCONDITION
from webhook.protos.pogoprotos.map.weather.weather_alert_pb2 import _WEATHERALERT_SEVERITY

from webhook.protos.pogoprotos.enums.team_color_pb2 import _TEAMCOLOR
from webhook.protos.pogoprotos.enums.pokemon_id_pb2 import _POKEMONID
from webhook.protos.pogoprotos.enums.pokemon_move_pb2 import _POKEMONMOVE
from webhook.protos.pogoprotos.enums.raid_level_pb2 import _RAIDLEVEL
from webhook.protos.pogoprotos.enums.gender_pb2 import _GENDER
from webhook.protos.pogoprotos.enums.form_pb2 import _FORM
from webhook.protos.pogoprotos.enums.costume_pb2 import _COSTUME
from webhook.protos.pogoprotos.enums.weather_condition_pb2 import _WEATHERCONDITION
from webhook.protos.pogoprotos.enums.quest_type_pb2 import _QUESTTYPE
from webhook.protos.pogoprotos.data.quests.quest_reward_pb2 import _QUESTREWARD_TYPE
from webhook.protos.pogoprotos.inventory.item.item_id_pb2 import _ITEMID
from webhook.protos.pogoprotos.data.quests.quest_condition_pb2 import _QUESTCONDITION_CONDITIONTYPE
from webhook.protos.pogoprotos.enums.pokemon_type_pb2 import _POKEMONTYPE
from webhook.protos.pogoprotos.enums.activity_type_pb2 import _ACTIVITYTYPE

log = logging.getLogger(__name__)
compress = Compress()


class Webhook(Flask):

    def __init__(self, import_name, **kwargs):
        super(Webhook, self).__init__(import_name, **kwargs)
        compress.init_app(self)

        # Routes
        self.json_encoder = CustomJSONEncoder
        self.route("/webhook", methods=['GET', 'POST'])(self.webhook)

    def webhook(self):
        args = get_args()
        
        if request.method == "GET":
            request_json = request.args
        else:
            request_json = request.get_json()

        if args.log_webhook:
            log.info('Full webhook: ' + (json.dumps(request_json, sort_keys=True)))

        if "protos" in request_json:
            protos = request_json.get('protos')
        else:
            protos = request_json.get('contents')
            
        if "trainerlvl" in request_json:
            trainerlvl = request_json.get('trainerlvl', 30)
        else:
            trainerlvl = request_json.get('trainerLevel', 30)


        if protos:
            return self.parse_map_protos(protos, trainerlvl)
        else:
            return 'Listening for webhooks'

    def parse_map_protos(self, protos_dict, trainerlvl):
        args = get_args()
        method = 0

        for proto in protos_dict:
            if "method" in proto:
                method = proto['method']

            if "GetMapObjects" in proto or method == 106:
                if "GetMapObjects" in proto:
                    if args.log_gmo_enc:
                        log.info('Encoded GetMapObjects: ' + proto['GetMapObjects'])
                    gmo_response_string = b64decode(proto['GetMapObjects'])
                elif method == 106:
                    if args.log_gmo_enc:
                        log.info('Encoded GetMapObjects: ' + proto['data'])
                    gmo_response_string = b64decode(proto['data'])

                gmo = GetMapObjectsResponse()

                try:
                    gmo.ParseFromString(gmo_response_string)
                    gmo_response_json = json.loads(MessageToJson(gmo))
                except:
                    continue

                if args.log_gmo_par:
                    log.info('Parsed GetMapObjects: ' + (json.dumps(gmo_response_json, sort_keys=True)))

            if "GetPlayerResponse" in proto or method == 2:
                if "GetPlayerResponse" in proto:
                    if args.log_gpr_enc:
                        log.info('Encoded GetPlayerResponse: ' + proto['GetPlayerResponse'])
                    get_player_response_string = b64decode(proto['GetPlayerResponse'])
                elif method == 2:
                    if args.log_gpr_enc:
                        log.info('Encoded GetPlayerResponse: ' + proto['data'])
                    get_player_response_string = b64decode(proto['data'])

                gpr = GetPlayerResponse()

                try:
                    gpr.ParseFromString(get_player_response_string)
                    get_player_response_json = json.loads(MessageToJson(gpr))
                except:
                    continue

                if args.log_gpr_par:
                    log.info('Parsed GetPlayerResponse: ' + (json.dumps(get_player_response_json, sort_keys=True)))

            if "GymGetInfoResponse" in proto or method == 156:
                if "GymGetInfoResponse" in proto:
                    if args.log_ggir_enc:
                        log.info('Encoded GymGetInfoResponse: ' + proto['GymGetInfoResponse'])
                    gym_get_info_response_string = b64decode(proto['GymGetInfoResponse'])
                elif method == 156:
                    if args.log_ggir_enc:
                        log.info('Encoded GymGetInfoResponse: ' + proto['data'])
                    gym_get_info_response_string = b64decode(proto['data'])


                ggir = GymGetInfoResponse()

                try:
                    ggir.ParseFromString(gym_get_info_response_string)
                    gym_get_info_response_json = json.loads(MessageToJson(ggir))
                except:
                    continue

                if args.log_ggir_par:
                    log.info('Parsed GymGetInfoResponse: ' + (json.dumps(gym_get_info_response_json, sort_keys=True)))

            if "FortDetailsResponse" in proto or method == 104:
                if "FortDetailsResponse" in proto:
                    if args.log_fdr_enc:
                        log.info('Encoded FortDetailsResponse: ' + proto['FortDetailsResponse'])
                    fort_details_response_string = b64decode(proto['FortDetailsResponse'])
                elif method == 104:
                    if args.log_fdr_enc:
                        log.info('Encoded FortDetailsResponse: ' + proto['data'])
                    fort_details_response_string = b64decode(proto['data'])


                fdr = FortDetailsResponse()

                try:
                    fdr.ParseFromString(fort_details_response_string)
                    fort_details_response_json = json.loads(MessageToJson(fdr))
                except:
                    continue

                if args.log_fdr_par:
                    log.info('Parsed FortDetailsResponse: ' + (json.dumps(fort_details_response_json, sort_keys=True)))

            if "FortSearchResponse" in proto or method == 101:
                if "FortSearchResponse" in proto:
                    if args.log_frs_enc:
                        log.info('Encoded FortSearchResponse: ' + proto['FortSearchResponse'])
                    fort_search_response_string = b64decode(proto['FortSearchResponse'])
                elif method == 101:
                    if args.log_frs_enc:
                        log.info('Encoded FortSearchResponse: ' + proto['data'])
                    fort_search_response_string = b64decode(proto['data'])


                frs = FortSearchResponse()

                try:
                    frs.ParseFromString(fort_search_response_string)
                    fort_search_response_json = json.loads(MessageToJson(frs))
                except:
                    continue

                if args.log_frs_par:
                    log.info('Parsed FortSearchResponse: ' + (json.dumps(fort_search_response_json, sort_keys=True)))

            if ("EncounterResponse" in proto or method == 102) and int(trainerlvl) >= 30:
                if "EncounterResponse" in proto:
                    if args.log_encounter_enc:
                        log.info('Encoded EncounterResponse: ' + proto['EncounterResponse'])
                    encounter_response_string = b64decode(proto['EncounterResponse'])
                elif method == 102:
                    if args.log_encounter_enc:
                        log.info('Encoded EncounterResponse: ' + proto['data'])
                    encounter_response_string = b64decode(proto['data'])

                encounter = EncounterResponse()

                try:
                    encounter.ParseFromString(encounter_response_string)
                    encounter_response_json = json.loads(MessageToJson(encounter))
                except:
                    continue

                if args.log_encounter_par:
                    log.info('Parsed EncounterResponse: ' + (json.dumps(encounter_response_json, sort_keys=True)))

        return 'ok'

class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, datetime):
                if obj.utcoffset() is not None:
                    obj = obj - obj.utcoffset()
                millis = int(
                    calendar.timegm(obj.timetuple()) * 1000 +
                    obj.microsecond / 1000
                )
                return millis
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)
