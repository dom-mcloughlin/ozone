class StringManager(object):
    def __init__(self):
        self.date = "Date"
        self.WSR0 = "WSR0"
        self.WSR1 = "WSR1"
        self.WSR2 = "WSR2"
        self.WSR3 = "WSR3"
        self.WSR4 = "WSR4"
        self.WSR5 = "WSR5"
        self.WSR6 = "WSR6"
        self.WSR7 = "WSR7"
        self.WSR8 = "WSR8"
        self.WSR9 = "WSR9"
        self.WSR10 = "WSR10"
        self.WSR11 = "WSR11"
        self.WSR12 = "WSR12"
        self.WSR13 = "WSR13"
        self.WSR14 = "WSR14"
        self.WSR15 = "WSR15"
        self.WSR16 = "WSR16"
        self.WSR17 = "WSR17"
        self.WSR18 = "WSR18"
        self.WSR19 = "WSR19"
        self.WSR20 = "WSR20"
        self.WSR21 = "WSR21"
        self.WSR22 = "WSR22"
        self.WSR23 = "WSR23"
        self.WSR_PK = "WSR_PK"
        self.WSR_AV = "WSR_AV"
        self.T0 = "T0"
        self.T1 = "T1"
        self.T2 = "T2"
        self.T3 = "T3"
        self.T4 = "T4"
        self.T5 = "T5"
        self.T6 = "T6"
        self.T7 = "T7"
        self.T8 = "T8"
        self.T9 = "T9"
        self.T10 = "T10"
        self.T11 = "T11"
        self.T12 = "T12"
        self.T13 = "T13"
        self.T14 = "T14"
        self.T15 = "T15"
        self.T16 = "T16"
        self.T17 = "T17"
        self.T18 = "T18"
        self.T19 = "T19"
        self.T20 = "T20"
        self.T21 = "T21"
        self.T22 = "T22"
        self.T23 = "T23"
        self.T_PK = "T_PK"
        self.T_AV = "T_AV"
        self.T85 = "T85"
        self.RH85 = "RH85"
        self.U85 = "U85"
        self.V85 = "V85"
        self.HT85 = "HT85"
        self.T70 = "T70"
        self.RH70 = "RH70"
        self.U70 = "U70"
        self.V70 = "V70"
        self.HT70 = "HT70"
        self.T50 = "T50"
        self.RH50 = "RH50"
        self.U50 = "U50"
        self.V50 = "V50"
        self.HT50 = "HT50"
        self.KI = "KI"
        self.TT = "TT"
        self.SLP = "SLP"
        self.SLP_ = "SLP_"
        self.precipitation = "Precp"
        self.ozone = "Ozone"
        return

    def float_columns(self):
        return_values = [
            self.WSR0,
            self.WSR1,
            self.WSR2,
            self.WSR3,
            self.WSR4,
            self.WSR5,
            self.WSR6,
            self.WSR7,
            self.WSR8,
            self.WSR9,
            self.WSR10,
            self.WSR11,
            self.WSR12,
            self.WSR13,
            self.WSR14,
            self.WSR15,
            self.WSR16,
            self.WSR17,
            self.WSR18,
            self.WSR19,
            self.WSR20,
            self.WSR21,
            self.WSR22,
            self.WSR23,
            self.WSR_PK,
            self.WSR_AV,
            self.T0,
            self.T1,
            self.T2,
            self.T3,
            self.T4,
            self.T5,
            self.T6,
            self.T7,
            self.T8,
            self.T9,
            self.T10,
            self.T11,
            self.T12,
            self.T13,
            self.T14,
            self.T15,
            self.T16,
            self.T17,
            self.T18,
            self.T19,
            self.T20,
            self.T21,
            self.T22,
            self.T23,
            self.T_PK,
            self.T_AV,
            self.T85,
            self.RH85,
            self.U85,
            self.V85,
            self.HT85,
            self.T70,
            self.RH70,
            self.U70,
            self.V70,
            self.HT70,
            self.T50,
            self.RH50,
            self.U50,
            self.V50,
            self.HT50,
            self.KI,
            self.TT,
            self.SLP,
            self.SLP_,
            self.precipitation,
        ]
        return return_values


strings = StringManager()
