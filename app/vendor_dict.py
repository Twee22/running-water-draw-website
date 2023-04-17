from app import app
from app.models import Vendor

vendor_dict = {

#Row 3
    "booth_128": {
    "booth_num": 128,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_1": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_115": {"booth_num": 115, "business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_116": {
    "booth_num": 116,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_2": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_119": {
    "booth_num": 119,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_120": {
    "booth_num": 120,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_3": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_123": {
    "booth_num": 123,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_124": {
    "booth_num": 124,"business_name": "NOTINIT", "status": "NOTINIT"
    },

#Row 4
    "filler_4": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "filler_5": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_126": {
    "booth_num": 126,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_6": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_113": {
    "booth_num": 113,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_114": {
    "booth_num": 114,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_7": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_117": {
    "booth_num": 117,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_118": {
    "booth_num": 118,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_8": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_121": {
    "booth_num": 121,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_122": {
    "booth_num": 122,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_9": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "filler_10": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
     
#Row 5
    "booth_126_2": {
    "booth_num": 126,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_11": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_12": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_13": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_14": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_15": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_16": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_17": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_18": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_19": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_20": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_21": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, 
    
#Row 6
    "booth_125": {
    "booth_num": 125,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_22": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_103": {
    "booth_num": 103,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_104": {
    "booth_num": 104,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_23": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_107": {
    "booth_num": 107,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_108": {
    "booth_num": 108,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_24": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_111": {
    "booth_num": 111,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_112": {
    "booth_num": 112,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_25": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "filler_26": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    

#Row 7
    "filler_27": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "filler_28": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_101": {
    "booth_num": 101,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_102": {
    "booth_num": 102,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_29": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_105": {
    "booth_num": 105,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_106": {
    "booth_num": 106,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_30": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_109": {
    "booth_num": 109,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_110": {
    "booth_num": 110,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_31": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "filler_32": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },


#Row 8
    "filler_33": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_34": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_35": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_36": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_37": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_38": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_39": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_40": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_41": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_42": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_43": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_44": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"},


#Row 9
    "booth_88": {
    "booth_num": 88,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_45": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_91": {
    "booth_num": 91,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_92": {
    "booth_num": 92,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_46": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_95": {
    "booth_num": 95,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_96": {
    "booth_num": 96,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_47": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_99": {
    "booth_num": 99,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_100": {
    "booth_num": 100,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_48": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "filler_49": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },


#Row 10
    "filler_50": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "filler_51": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_89": {
    "booth_num": 89,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_90": {
    "booth_num": 90,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_52": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_93": {
    "booth_num": 93,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_94": {
    "booth_num": 94,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_53": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_97": {
    "booth_num": 97,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "booth_98": {
    "booth_num": 98,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    "filler_54": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "filler_55": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },


#Row 11
    "filler_56": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_57": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_58": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_59": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_60": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_61": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_62": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_63": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_64": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_65": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, "filler_66": {"booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"}, 
    
    "booth_86": {
    "booth_num": 86,"business_name": "NOTINIT", "status": "NOTINIT"
    },
    


#Row 12
    "filler_67": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "filler_68": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "filler_69": {
    "booth_num": 0, "business_name": "NOTINIT", "status": "FILLER"
    },
    "booth_76":{
    "booth_num": 76,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "filler_70": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "booth_79":{
    "booth_num": 79,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "booth_80":{
    "booth_num": 80,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "filler_71": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "booth_83":{
    "booth_num": 83,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "booth_84":{
    "booth_num": 84,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "filler_72": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "booth_85":{
    "booth_num": 85,"business_name": "NOTINIT","status": "NOTINIT"
    },


#Row 13
    "filler_73": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "filler_74": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "filler_75": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "booth_75":{
    "booth_num": 75,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "filler_76": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "booth_77":{
    "booth_num": 77,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "booth_78":{
    "booth_num": 78,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "filler_77": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "booth_81":{
    "booth_num": 81,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "booth_82":{
    "booth_num": 82,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "filler_78": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "filler_79": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },


#Row 14
    "booth_46":{
    "booth_num": 46,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "filler_80": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "filler_81": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "filler_82": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "filler_83": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "filler_84": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "filler_85": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "filler_86": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "filler_87": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "filler_88": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "filler_89": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "filler_90": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },


#Row 15
    "booth_45":{
    "booth_num": 45,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "filler_91": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "booth_65":{
    "booth_num": 65,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "booth_66":{
    "booth_num": 66,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "filler_92": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "booth_69":{
    "booth_num": 69,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "booth_70":{
    "booth_num": 70,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "filler_93": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "booth_73":{
    "booth_num": 73,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "booth_74":{
    "booth_num": 74,"business_name": "NOTINIT","status": "NOTINIT"
    },
    "filler_94": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },
    "filler_95": {
    "booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    },


#Row 16
    "booth_44":{
	"booth_num": 44,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_96": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_63":{
	"booth_num": 63,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_64":{
	"booth_num": 64,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_97": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_67":{
	"booth_num": 67,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_68":{
	"booth_num": 68,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_98": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_71":{
	"booth_num": 71,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_72":{
	"booth_num": 72,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_99": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_50":{
	"booth_num": 50,"business_name": "NOTINIT","status": "NOTINIT"
	},


#Row 17
	"booth_43":{
	"booth_num": 43,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_100": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_101": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_102": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_103": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_104": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_105": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_106": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_107": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_108": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_109": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_49":{
	"booth_num": 49,"business_name": "NOTINIT","status": "NOTINIT"
	},

#Row 18
	"booth_42":{
	"booth_num": 42,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_110": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_53":{
	"booth_num": 53,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_54":{
	"booth_num": 54,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_111": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_57":{
	"booth_num": 57,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_58":{
	"booth_num": 58,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_112": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_61":{
	"booth_num": 61,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_62":{
	"booth_num": 62,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_113": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_48":{
	"booth_num": 48,"business_name": "NOTINIT","status": "NOTINIT"
	},


#Row 19
	"booth_41":{
	"booth_num": 41,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_114": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_51":{
	"booth_num": 51,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_52":{
	"booth_num": 52,"business_name": "NOTINIT", "status": "NOTINIT"
	},
	"filler_115": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_55":{
	"booth_num": 55,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_56":{
	"booth_num": 56,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_116": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_59":{
	"booth_num": 59,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_60":{
	"booth_num": 60,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_117": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_118": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},


#Row 20
    "filler_119": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_120": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_121": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_122": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_123": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_124": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_125": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_126": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_127": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_128": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_129": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_130": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},


#Row 21
	"filler_131": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_132": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_31":{
	"booth_num": 31,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_32":{
	"booth_num": 32,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_133": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_35":{
	"booth_num": 35,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_36":{
	"booth_num": 36,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_134": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_39":{
	"booth_num": 39,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_40":{
	"booth_num": 40,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_135": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_15":{
	"booth_num": 15,"business_name": "NOTINIT","status": "NOTINIT"
	},


#Row 22
	"booth_10":{
	"booth_num": 10,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_136": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_29":{
	"booth_num": 29,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_30":{
	"booth_num": 30,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_137": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_33":{
	"booth_num": 33,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_34":{
	"booth_num": 34,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_138": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_37":{
	"booth_num": 37,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_38":{
	"booth_num": 38,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_139": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_14":{
	"booth_num": 14,"business_name": "NOTINIT","status": "NOTINIT"
	},


#Row 23
	"booth_9":{
	"booth_num": 9,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_140": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_141": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_142": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_143": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_144": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_145": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_146": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_147": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_148": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_149": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_13":{
	"booth_num": 13,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_8":{
	"booth_num": 8,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_150": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_19":{
	"booth_num": 19,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_20":{
	"booth_num": 20,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_151": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_23":{
	"booth_num": 23,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_24":{
	"booth_num": 24,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_152": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_27":{
	"booth_num": 27,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_28":{
	"booth_num": 28,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_153": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_12":{
	"booth_num": 12,"business_name": "NOTINIT","status": "NOTINIT"
	},


#Row 24
	"booth_7":{
	"booth_num": 7,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_154": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_17":{
	"booth_num": 17,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_18":{
	"booth_num": 18,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_155": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_21":{
	"booth_num": 21,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_22":{
	"booth_num": 22,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_156": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_25":{
	"booth_num": 25,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_26":{
	"booth_num": 26,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_157": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_158": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},


#Row 25    
    "filler_159": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_160": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_161": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_162": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_163": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_164": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_165": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_166": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_167": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_168": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_169": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_170": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},


#Row 26
	"filler_171": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_172": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"booth_6":{
	"booth_num": 6,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_5":{
	"booth_num": 5,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_4":{
	"booth_num": 4,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_3":{
	"booth_num": 3,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_2":{
	"booth_num": 2,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"booth_1":{
	"booth_num": 1,"business_name": "NOTINIT","status": "NOTINIT"
	},
	"filler_173": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_174": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_175": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},
	"filler_176": {
	"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
	},

#Row 27
	"filler_177": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_178": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_179": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_180": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_181": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_182": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_183": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_184": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_185": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_186": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_187": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"},"filler_188": {"booth_num": 0,"business_name": "NOTINIT","status": "FILLER"
    }
}

# links dictionary to database, dictionary is updated everytime the database is updated
def update(vendors):
    
    for vendor in vendors: 
        for key in vendor_dict:
            if int(vendor.boothLoc) == vendor_dict[key]['booth_num']:
                if vendor.status == "pendingApproval" or "pendingPayment":
                    vendor_dict[key]['status'] = "PENDING"
                elif vendor.status == "finalized": 
                    vendor_dict[key]['business_name'] = vendor.business
                    vendor_dict[key]['status'] = "APPROVED"
    return vendor_dict