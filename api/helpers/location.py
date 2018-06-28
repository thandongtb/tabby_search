import random

locations = [
    {
        "location": "103G2 Hào Nam, Chợ Dừa, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.021934945353756,
        "lng": 105.82697001363182
    },
    {
        "location": "B5b Hoàng Ngọc Phách, Láng Hạ, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.015508489818043,
        "lng": 105.8126899534983
    },
    {
        "location": "128 Tôn Đức Thắng, Quốc Tử Giám, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.02616437327533,
        "lng": 105.83345442429714
    },
    {
        "location": "C8 Giảng Võ, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.024731307128008,
        "lng": 105.82080843923406
    },
    {
        "location": "Ngõ 33 Cát Linh, Cát Linh, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.028647715224015,
        "lng": 105.82888065141634
    },
    {
        "location": "2 Trần Huy Liệu, Giảng Võ, Ba Đình, Hà Nội, Vietnam",
        "lat": 21.028653680425872,
        "lng": 105.81974062889307
    },
    {
        "location": "145 Ngõ Văn Chương, Văn Chương, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.023272925536265,
        "lng": 105.83344249567611
    },
    {
        "location": "104 Cầu Vượt, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.016284967668007,
        "lng": 105.80576041679522
    },
    {
        "location": "50/159 Pháo Đài Láng, Láng Thượng, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.01855349809251,
        "lng": 105.80574792321048
    },
    {
        "location": "Ngõ 44 Pháo Đài Láng, Láng Thượng, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.021692170904135,
        "lng": 105.80374341416147
    },
    {
        "location": "45 Ngõ 221 Tôn Đức Thắng, Thổ Quan, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.021302769546995,
        "lng": 105.83244313152231
    },
    {
        "location": "371 Ngõ Văn Chương, Khâm Thiên, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.01975582469369,
        "lng": 105.83724543932759
    },
    {
        "location": "Ngõ 10 - Láng Hạ, Thành Công, Ba Đình, Hà Nội, Vietnam",
        "lat": 21.021777971329215,
        "lng": 105.81744926237823
    },
    {
        "location": "50 Nam Cao, Giảng Võ, Ba Đình, Hà Nội, Vietnam",
        "lat": 21.029427693176757,
        "lng": 105.82236097421021
    },
    {
        "location": "227 Nguyễn Khang, Yên Hoà, Cầu Giấy, Hà Nội, Vietnam",
        "lat": 21.02263159869527,
        "lng": 105.79891635603862
    },
    {
        "location": "66 Trung Kính, Yên Hoà, Cầu Giấy, Hà Nội, Vietnam",
        "lat": 21.015162750619794,
        "lng": 105.79504233461876
    },
    {
        "location": "63 Huỳnh Thúc Kháng, Láng Hạ, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.019338600821705,
        "lng": 105.80854640331792
    },
    {
        "location": "135/1194 Đường Láng, Láng Thượng, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.023798877527184,
        "lng": 105.80160878564034
    },
    {
        "location": "35 Nguyễn Chí Thanh, Ngọc Khánh, Ba Đình, Hà Nội, Vietnam",
        "lat": 21.02748375286323,
        "lng": 105.81197809567038
    },
    {
        "location": "15-17 Ngọc Khánh, Giảng Võ, Ba Đình, Hà Nội, Vietnam",
        "lat": 21.02934291578725,
        "lng": 105.81940897970134
    },
    {
        "location": "Ngõ 87 Nguyễn Khang, Yên Hoà, Cầu Giấy, Hà Nội, Vietnam",
        "lat": 21.0188740961614,
        "lng": 105.80122333097455
    },
    {
        "location": "50 Nam Cao, Giảng Võ, Ba Đình, Hà Nội, Vietnam",
        "lat": 21.029647208841574,
        "lng": 105.82244421702246
    },
    {
        "location": "25 Ngõ 98, Yên Hoà, Cầu Giấy, Hà Nội, Vietnam",
        "lat": 21.021007054676435,
        "lng": 105.79794803101379
    },
    {
        "location": "C9B - Nam Thành Công, Hoàng Ngọc Phách, Khu tập thể Nam Thành Công, Láng Hạ, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.016058653586093,
        "lng": 105.81119122280262
    },
    {
        "location": "55 Ngọc Khánh, Giảng Võ, Ba Đình, Hà Nội, Vietnam",
        "lat": 21.025197507887132,
        "lng": 105.81683260466575
    },
    {
        "location": "3/79 Ngõ Lương Sử A, Văn Chương, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.02586986578253,
        "lng": 105.83714247153767
    },
    {
        "location": "Ngõ 141 - Nguyễn Khang, Yên Hoà, Cầu Giấy, Hà Nội, Vietnam",
        "lat": 21.019618899704312,
        "lng": 105.7997159258092
    },
    {
        "location": "120 Ngõ Chùa Nền, Láng Thượng, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.02531096058347,
        "lng": 105.79992973206372
    },
    {
        "location": "52 Nam Cao, Giảng Võ, Ba Đình, Hà Nội, Vietnam",
        "lat": 21.029899230918417,
        "lng": 105.82235581859693
    },
    {
        "location": "Tòa nhà G4, Trung Hoà, Cầu Giấy, Hà Nội, Vietnam",
        "lat": 21.015444519517928,
        "lng": 105.79576929803797
    },
    {
        "location": "49 Láng Thượng, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.019636682019055,
        "lng": 105.80302004327217
    },
    {
        "location": "A1 Tập Thể Hào Nam, 211 A1 Tập Thể Hào Nam, Ngõ 8c Vũ Thạnh, Ô Chợ Dừa, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.026452275189044,
        "lng": 105.82502411067287
    },
    {
        "location": "55 Ngõ 1150 - Láng, Láng Thượng, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.024207181539065,
        "lng": 105.79971339019484
    },
    {
        "location": "1242 Đường Láng, Láng Thượng, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.029462686034933,
        "lng": 105.80160633331467
    },
    {
        "location": "90 Ngõ 34 Hoàng Cầu, Chợ Dừa, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.020614931545875,
        "lng": 105.82286512341156
    },
    {
        "location": "10 Phố Nguyễn Thái Học, Văn Miếu, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.029067023512905,
        "lng": 105.83882626985803
    },
    {
        "location": "36 Nguyên Hồng, Thành Công, Ba Đình, Hà Nội, Vietnam",
        "lat": 21.023611461378888,
        "lng": 105.81140404299451
    },
    {
        "location": "6 Ngọc Khánh, Giảng Võ, Ba Đình, Hà Nội, Vietnam",
        "lat": 21.026812320852848,
        "lng": 105.81837194922734
    },
    {
        "location": "16 Trần Kim Xuyến, Yên Hoà, Cầu Giấy, Hà Nội, Vietnam",
        "lat": 21.018405704436127,
        "lng": 105.79578880722573
    },
    {
        "location": "Ngõ 278, Hàng Bột, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.01993986007818,
        "lng": 105.83040626962902
    },
    {
        "location": "62 Phạm Huy Thông, Ngọc Khánh, Ba Đình, Hà Nội, Vietnam",
        "lat": 21.02715259572292,
        "lng": 105.80992395816317
    },
    {
        "location": "Ngõ 74 Nguyễn Chí Thanh, Láng Thượng, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.018351101182237,
        "lng": 105.80599398521939
    },
    {
        "location": "389 Nguyễn Khang, Yên Hoà, Cầu Giấy, Hà Nội, Vietnam",
        "lat": 21.02798643128743,
        "lng": 105.7984902142882
    },
    {
        "location": "A2/15 Ngọc Khánh, Giảng Võ, Ba Đình, Hà Nội, Vietnam",
        "lat": 21.029491760932036,
        "lng": 105.81834432109376
    },
    {
        "location": "66 Ngõ 360 Xã Đàn, Thổ Quan, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.015413100892516,
        "lng": 105.83546616287664
    },
    {
        "location": "153 tổ 9 Láng Thượng, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.02420271228422,
        "lng": 105.80064377876127
    },
    {
        "location": "91 Nguyễn Phúc Lai, Chợ Dừa, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.019339802752064,
        "lng": 105.82128612098231
    },
    {
        "location": "304 Mai Anh Tuấn, Chợ Dừa, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.018135874505113,
        "lng": 105.81799700536017
    },
    {
        "location": "87 Ngõ Quan Thổ 1, Hàng Bột, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.022272412825203,
        "lng": 105.82928919574827
    },
    {
        "location": "41 Đường Yên Hòa, Yên Hoà, Cầu Giấy, Hà Nội, Vietnam",
        "lat": 21.023319570079373,
        "lng": 105.79663535075534
    },
    {
        "location": "Ngõ 89, Láng Hạ, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.01508067704288,
        "lng": 105.80903261131634
    },
    {
        "location": "Cong ty CP Tham dinh gia BTCvalue - Suite 1706, DMC Tower, 535 Kim Mã, Ngọc Khánh, Ba Đình, Hà Nội, Vietnam",
        "lat": 21.02930949756909,
        "lng": 105.81001582377812
    },
    {
        "location": "110 Nguyên Hồng, Láng Hạ, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.015638883884737,
        "lng": 105.80977204806632
    },
    {
        "location": "112 Trần Huy Liệu, Giảng Võ, Ba Đình, Hà Nội, Vietnam",
        "lat": 21.02893670638576,
        "lng": 105.82009145981047
    },
    {
        "location": "300 Đê la Thành, Chợ Dừa, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.02189868233784,
        "lng": 105.82470676526955
    },
    {
        "location": "49 Ngõ Lương Sử A, Văn Chương, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.025808688788988,
        "lng": 105.83664032810464
    },
    {
        "location": "6 Ngõ 1194 - Láng, Láng Thượng, Đống Đa, Hà Nội, Vietnam",
        "lat": 21.026530994701787,
        "lng": 105.80371815621788
    }
]

def get_random_location():
    return random.choice(locations)