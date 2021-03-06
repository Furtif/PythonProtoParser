# Base Package Imports#
import os, sys
sys.path.append('./POGOProtosPython/')

import json, time
from base64 import b64decode, binascii
from datetime import datetime, timedelta

# Third Party Imports #
import google
from google.protobuf.json_format import MessageToJson

# Import from POGOProtosPython repo submodule ##
from pogoprotos.networking.responses.get_map_objects_response_pb2 import GetMapObjectsResponse
from pogoprotos.networking.responses.encounter_response_pb2 import EncounterResponse
from pogoprotos.networking.responses.fort_search_response_pb2 import FortSearchResponse
from pogoprotos.networking.responses.fort_details_response_pb2 import FortDetailsResponse
from pogoprotos.networking.responses.gym_get_info_response_pb2 import GymGetInfoResponse
from pogoprotos.networking.responses.get_player_response_pb2 import GetPlayerResponse
from pogoprotos.networking.responses.get_holo_inventory_response_pb2 import GetHoloInventoryResponse


# Start The Good Stuff #

def getKeyValue(dict,key):
    
    if key in dict.keys():
        return(dict[key])
    else:
        return(None)

## ProtoParser Class Begin ##
class ProtoParser(object):

    #Identify Proto type from iSpoofer #
    def mapProtoTypeIspoofer(self, method):

        if method == 101:
            return "FortSearchResponse"
        if method == 104:
            return "FortDetailsResponse"
        if method == 106:
            return "GetMapObjects"
        if method == 156:
            return "GymGetInfoResponse"
        if method == 102:
            return "EncounterResponse"
        if method == 4:
            return "GET_HOLOHOLO_INVENTORY"
        if method == 2:
            return "GetPlayerResponse"

    ## Actual Parsing Call ##     
    def parseProtos(self,raw_resp):

        data = list()

        ProtoType = ""
        #Handle Ispoofer Proto Wrapper
        if "contents" in raw_resp:
            responseType = "Ispoofer"
            for l in raw_resp['contents']:
                ProtoType = self.mapProtoTypeIspoofer(l['method'])
                ProtoData = l['data']
                data.append({"Type": ProtoType, "Data":ProtoData})
            

        
        if "protos" in raw_resp:
            responseType = "PlusPlus"
            for p in raw_resp['protos']:
                for p2 in p:
                    ProtoType = p2
                    ProtoData = p[ProtoType]
                    data.append({"Type": ProtoType, "Data":ProtoData})
            
        if responseType == "PlusPlus":
            latTarget = raw_resp['latitude']
            lonTarget = raw_resp['longitude']
            level = raw_resp['trainerlvl']
            time_recieved = raw_resp['timestamp']

        if responseType == "Ispoofer":
            level = raw_resp['trainerLevel']
            time_recieved = int(time.time())

        
        print("####################################")
        print("Parsing")
        print(ProtoType)
        print("From")
        print(responseType)
        print("####################################")
        
        
        
        #-Create Arrays to hold proto Objects of interest-#
        self.pokestops = []
        self.gyms = []
        cells = []
        encounters = []
        self.wildPokemons = []
        self.nearbyPokemons = []
               
        if responseType == "PlusPlus":
            proto_list = raw_resp['protos']
        if responseType == "Ispoofer":
            proto_list = raw_resp['contents']

        for D in data:
            ## GMO Parsing Block ##
            if D["Type"] == "GetMapObjects" :
                
                raw_gmo = D["Data"]
                
                try:
                    gmo_str = b64decode(raw_gmo)
                except binascii.Error as e:
                    print("[Error]:[Webhook-Parser] Reference: " + str(e))
                    continue
                
                try:
                    GMO = GetMapObjectsResponse()
                    gmo = GMO.FromString(gmo_str)
                except google.protobuf.message.Error as e:
                    print("[Error]:[Webhook-Parser] Reference: +" + str(e))
                    continue
                
                
                gmo_json = json.loads(MessageToJson(gmo))
                
            ## Encounter Response Parsing Block ##    
            elif D["Type"] == "EncounterResponse":
                
                try:
                    raw_enc = D["Data"]
                    enc_str = b64decode(raw_enc)
                except binascii.Error as e:
                    print("[Error]:[Webhook-Parser] Reference: " + str(e))
                    continue
                try:
                    EncResp = EncounterResponse()
                    enc_class = EncounterResponse.FromString(enc_str)
                    enc_json = json.loads(MessageToJson(enc_class))
                    return(enc_json)
                except google.protobuf.message.Error as e:
                    print("[Error]:[Webhook-Parser] Reference: " + str(e))
                    continue
                
            ## FortDetailsResponse(Open Stop) Parsing Block ##
            elif D["Type"] == "FortDetailsResponse":
                
                try:
                    raw_fdr = D["Data"]
                    fdr_str = b64decode(raw_fdr)
                except binascii.Error as e:
                    print("[Error]:[Webhook-Parser] Response: " + str(e))
                    continue
                try:
                    FDR = FortDetailsResponse()
                    fdr = FDR.FromString(fdr_str)
                    fdr_json = json.loads(MessageToJson(fdr))
                    return(fdr_json)
                except google.protobuf.message.Error as e:
                    print("[Error]:[Webhook-Parser] Response: " + str(e))
                    continue
                
            ## FortSearchResponse (Spun Stop) Parsing Block ##    
            elif D["Type"] == "FortSearchResponse" :
                
                try:
                    raw_fsr = D["Data"]
                    fsr_str = b64decode(raw_fsr)
                except binascii.Error as e:
                    print("[Error]:[Webhook-Parser] Response: " + str(e))
                    continue
                try:
                    FSR = FortSearchResponse()
                    fsr = FSR.FromString(fsr_str)
                    fsr_json = json.loads(MessageToJson(fsr))
                    return(fsr_json)
                except google.protobuf.message.Error as e:
                    print("[Error]:[Webhook-Parser: Response: " + str(e))
                    continue
                
            ## GetPlayerResponse ##
            elif D["Type"] == "GetPlayerResponse":
                try:
                    raw_gpr = D["Data"]
                    gpr_str = b64decode(raw_gpr)
                except binascii.Error as e:
                    print("[Error]:[Webhook-Parser] Response: " + str(e))
                    continue
                try:
                    GPR = GetPlayerResponse()
                    gpr = GPR.FromString(gpr_str)
                    gpr_json = json.loads(MessageToJson(gpr))
                    return(gpr_json)
                except google.protobuf.message.Error as e:
                    print("[Error]:[Webhook-Parser: GetPlayerResponse] " + str(e))
                    continue
            
            ## GetHoloInventoryResponse Parsing Block (iSpoofer Only)
            elif D["Type"] == "GET_HOLOHOLO_INVENTORY":
                try:
                    raw_inv = D["Data"]
                    inv_str = b64decode(raw_inv)
                except binascii.Error as e:
                    print("[Error]:[Webhook-Parser] Response: " + str(e))
                    continue
                try:
                    INV = GetHoloInventoryResponse()
                    inv = INV.FromString(inv_str)
                    inv_json = json.loads(MessageToString(inv_json))
                    return(inv_json)
                except google.protobuf.message.Error as e:
                    print("[Error]:[Webhook-Parser: GetPlayerResponse] " + str(e))
                    continue

            ## GymGetInfoResponse Start Block #GymDefenders! ##
            elif D["Type"] == "GymGetInfoResponse":
                try:
                    raw_ggir = D["Data"]
                    ggir_str = b64decode(raw_ggir)
                except binascii.Error as e:
                    print("[Error]:[Webhook-Parser] Response: " + str(e))
                    continue
                try:
                    GGIR = GymGetInfoResponse()
                    ggir = GGIR.FromString(ggir_str)
                    gym_json = json.loads(MessageToJson(ggir))
                    gym_formatted = formatDefenders(gym_json)
                    return(gym_json)
                except google.protobuf.message.Error as e:
                    print("[Error]:[Webhook-Parser: GymGetInfoResponse] " + str(e))
                    continue
            else:
                print("[Info]: Response is empty, or contains unsupported protos")
