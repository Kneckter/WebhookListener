#!/usr/bin/python
# -*- coding: utf-8 -*-

import calendar
import logging
import gc
import pprint

from datetime import datetime
from flask import Flask, request, json
from flask.json import JSONEncoder
from flask_compress import Compress
from base64 import b64decode
from webhook.utils import get_args

from google.protobuf.json_format import MessageToJson
from webhook.protos.pogoprotos.networking.responses.get_player_response_pb2 import GetPlayerResponse
from webhook.protos.pogoprotos.networking.responses.get_holo_inventory_response_pb2 import GetHoloInventoryResponse
from webhook.protos.pogoprotos.networking.responses.fort_search_response_pb2 import FortSearchResponse
from webhook.protos.pogoprotos.networking.responses.encounter_response_pb2 import EncounterResponse
from webhook.protos.pogoprotos.networking.responses.catch_pokemon_response_pb2 import CatchPokemonResponse
from webhook.protos.pogoprotos.networking.responses.fort_details_response_pb2 import FortDetailsResponse
from webhook.protos.pogoprotos.networking.responses.get_map_objects_response_pb2 import GetMapObjectsResponse
from webhook.protos.pogoprotos.networking.responses.recycle_inventory_item_response_pb2 import RecycleInventoryItemResponse
from webhook.protos.pogoprotos.networking.responses.disk_encounter_response_pb2 import DiskEncounterResponse
from webhook.protos.pogoprotos.networking.responses.gym_get_info_response_pb2 import GymGetInfoResponse
from webhook.protos.pogoprotos.networking.responses.get_raid_details_response_pb2 import GetRaidDetailsResponse
from webhook.protos.pogoprotos.networking.responses.remove_quest_response_pb2 import RemoveQuestResponse

log = logging.getLogger(__name__)
compress = Compress()


class Webhook(Flask):

    def __init__(self, import_name, **kwargs):
        super(Webhook, self).__init__(import_name, **kwargs)
        compress.init_app(self)

        # Routes
        self.json_encoder = CustomJSONEncoder
        self.route("/", methods=['GET', 'POST', 'CONNECT'])(self.webhook)
        self.route("/activate", methods=['GET', 'POST', 'CONNECT'])(self.webhook)
        self.route("/webhook", methods=['GET', 'POST', 'CONNECT'])(self.webhook)

    def webhook(self):
        args = get_args()
#        log.info(pprint.pformat(request.__dict__, depth=5))
#        log.info('Request: %s', request)
#        log.info('Environ: %s', request.environ)
#        log.info('Headers: %s', request.headers)
#        log.info('Body: %s', request.get_data())
#        log.info('Data: %s', request.get_json(request.data))
        
        if request.method == "GET":
            request_json = request.args
        elif request.method == "POST":
            request_json = request.get_json(request.get_data())
        else:
            request_json = request.get_json(request.get_data())

        if args.log_webhook:
            log.info('Full webhook: ' + (json.dumps(request_json, sort_keys=True)))

        if "protos" in request_json:
            protos = request_json.get('protos')
        elif "contents" in request_json:
            protos = request_json.get('contents')
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

            if ("GetPlayerResponse" in proto or method == 2) and (args.log_gpr_enc or args.log_gpr_par):
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

            if ("GetHoloInventoryResponse" in proto or method == 4) and (args.log_ghir_enc or args.log_ghir_par):
                if "GetHoloInventoryResponse" in proto:
                    if args.log_ghir_enc:
                        log.info('Encoded GetHoloInventoryResponse: ' + proto['GetHoloInventoryResponse'])
                    get_holo_inventory_response_string = b64decode(proto['GetHoloInventoryResponse'])
                elif method == 4:
                    if args.log_ghir_enc:
                        log.info('Encoded GetHoloInventoryResponse: ' + proto['data'])
                    get_holo_inventory_response_string = b64decode(proto['data'])

                ghir = GetHoloInventoryResponse()

                try:
                    ghir.ParseFromString(get_holo_inventory_response_string)
                    get_holo_inventory_response_json = json.loads(MessageToJson(ghir))
                except:
                    continue

                if args.log_ghir_par:
                    log.info('Parsed GetHoloInventoryResponse: ' + (json.dumps(get_holo_inventory_response_json, sort_keys=True)))

            if ("FortSearchResponse" in proto or method == 101) and (args.log_fsr_enc or args.log_fsr_par):
                if "FortSearchResponse" in proto:
                    if args.log_fsr_enc:
                        log.info('Encoded FortSearchResponse: ' + proto['FortSearchResponse'])
                    fort_search_response_string = b64decode(proto['FortSearchResponse'])
                elif method == 101:
                    if args.log_fsr_enc:
                        log.info('Encoded FortSearchResponse: ' + proto['data'])
                    fort_search_response_string = b64decode(proto['data'])

                frs = FortSearchResponse()

                try:
                    frs.ParseFromString(fort_search_response_string)
                    fort_search_response_json = json.loads(MessageToJson(frs))
                except:
                    continue

                if args.log_fsr_par:
                    log.info('Parsed FortSearchResponse: ' + (json.dumps(fort_search_response_json, sort_keys=True)))

            if ("EncounterResponse" in proto or method == 102) and (args.log_encounter_enc or args.log_encounter_par) and int(trainerlvl) >= args.trainerlvl:
                log.info('Logging')
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

            if ("CatchPokemonResponse" in proto or method == 103) and (args.log_cpr_enc or args.log_cpr_par):
                if "CatchPokemonResponse" in proto:
                    if args.log_cpr_enc:
                        log.info('Encoded CatchPokemonResponse: ' + proto['CatchPokemonResponse'])
                    catch_pokemon_response_string = b64decode(proto['CatchPokemonResponse'])
                elif method == 103:
                    if args.log_cpr_enc:
                        log.info('Encoded CatchPokemonResponse: ' + proto['data'])
                    catch_pokemon_response_string = b64decode(proto['data'])

                cpr = CatchPokemonResponse()

                try:
                    cpr.ParseFromString(catch_pokemon_response_string)
                    catch_pokemon_response_json = json.loads(MessageToJson(cpr))
                except:
                    continue

                if args.log_cpr_par:
                    log.info('Parsed CatchPokemonResponse: ' + (json.dumps(catch_pokemon_response_json, sort_keys=True)))

            if ("FortDetailsResponse" in proto or method == 104) and (args.log_fdr_enc or args.log_fdr_par):
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

            if ("GetMapObjects" in proto or method == 106) and (args.log_gmo_enc or args.log_gmo_par):
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

            if ("RecycleInventoryItemResponse" in proto or method == 137) and (args.log_riir_enc or args.log_riir_par):
                if "RecycleInventoryItemResponse" in proto:
                    if args.log_riir_enc:
                        log.info('Encoded RecycleInventoryItemResponse: ' + proto['RecycleInventoryItemResponse'])
                    recycle_inventory_item_response_string = b64decode(proto['RecycleInventoryItemResponse'])
                elif method == 137:
                    if args.log_riir_enc:
                        log.info('Encoded RecycleInventoryItemResponse: ' + proto['data'])
                    recycle_inventory_item_response_string = b64decode(proto['data'])

                riir = RecycleInventoryItemResponse()

                try:
                    riir.ParseFromString(recycle_inventory_item_response_string)
                    recycle_inventory_item_response_json = json.loads(MessageToJson(riir))
                except:
                    continue

                if args.log_riir_par:
                    log.info('Parsed RecycleInventoryItemResponse: ' + (json.dumps(recycle_inventory_item_response_json, sort_keys=True)))

            if ("DiskEncounterResponse" in proto or method == 145) and (args.log_der_enc or args.log_der_par):
                if "DiskEncounterResponse" in proto:
                    if args.log_der_enc:
                        log.info('Encoded DiskEncounterResponse: ' + proto['DiskEncounterResponse'])
                    disk_encounter_response_string = b64decode(proto['DiskEncounterResponse'])
                elif method == 145:
                    if args.log_der_enc:
                        log.info('Encoded DiskEncounterResponse: ' + proto['data'])
                    disk_encounter_response_string = b64decode(proto['data'])

                der = DiskEncounterResponse()

                try:
                    der.ParseFromString(disk_encounter_response_string)
                    disk_encounter_response_json = json.loads(MessageToJson(der))
                except:
                    continue

                if args.log_der_par:
                    log.info('Parsed DiskEncounterResponse: ' + (json.dumps(disk_encounter_response_json, sort_keys=True)))

            if ("GymGetInfoResponse" in proto or method == 156) and (args.log_ggir_enc or args.log_ggir_par):
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

            if ("GetRaidDetailsResponse" in proto or method == 163) and (args.log_grdr_enc or args.log_grdr_par):
                if "GetRaidDetailsResponse" in proto:
                    if args.log_grdr_enc:
                        log.info('Encoded GetRaidDetailsResponse: ' + proto['GetRaidDetailsResponse'])
                    get_raid_details_response_string = b64decode(proto['GetRaidDetailsResponse'])
                elif method == 163:
                    if args.log_grdr_enc:
                        log.info('Encoded GetRaidDetailsResponse: ' + proto['data'])
                    get_raid_details_response_string = b64decode(proto['data'])

                grdr = GetRaidDetailsResponse()

                try:
                    grdr.ParseFromString(get_raid_details_response_string)
                    get_raid_details_response_json = json.loads(MessageToJson(grdr))
                except:
                    continue

                if args.log_grdr_par:
                    log.info('Parsed GetRaidDetailsResponse: ' + (json.dumps(get_raid_details_response_json, sort_keys=True)))

            if ("RemoveQuestResponse" in proto or method == 903) and (args.log_rqr_enc or args.log_rqr_par):
                if "RemoveQuestResponse" in proto:
                    if args.log_rqr_enc:
                        log.info('Encoded RemoveQuestResponse: ' + proto['RemoveQuestResponse'])
                    remove_quest_response_string = b64decode(proto['RemoveQuestResponse'])
                elif method == 903:
                    if args.log_rqr_enc:
                        log.info('Encoded RemoveQuestResponse: ' + proto['data'])
                    remove_quest_response_string = b64decode(proto['data'])

                rqr = RemoveQuestResponse()

                try:
                    rqr.ParseFromString(remove_quest_response_string)
                    remove_quest_response_json = json.loads(MessageToJson(rqr))
                except:
                    continue

                if args.log_rqr_par:
                    log.info('Parsed RemoveQuestResponse: ' + (json.dumps(remove_quest_response_json, sort_keys=True)))

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
