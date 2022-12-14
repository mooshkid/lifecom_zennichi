# japan prefecture tuplets 
prefectures = [('01', '北海道'), ('02', '青森県'), ('03', '岩手県'), ('04', '宮城県'), ('05', '秋田県'), ('06', '山形県'), ('07', '福島県'), ('08', '茨城県'), ('09', '栃木県'), ('10', '群馬県'), ('11', '埼玉県'), ('12', '千葉県'), ('13', '東京都'), ('14', '神奈川県'), ('15', '山梨県'), ('16', '新潟県'), ('17', '富山県'), ('18', '石川県'), ('19', '福井県'), ('20', '長野県'), ('21', '岐阜県'), ('22', '静岡県'), ('23', '愛知県'), ('24', '三重県'), ('25', '滋賀県'), ('26', '京都府'), ('27', '大阪府'), ('28', '兵庫県'), ('29', '奈良県'), ('30', '和歌山県'), ('31', '鳥取県'), ('32', '島根県'), ('33', '岡山県'), ('34', '広島県'), ('35', '山口県'), ('36', '徳島県'), ('37', '香川県'), ('38', '愛媛県'), ('39', '高知県'), ('40', '福岡県'), ('41', '佐賀県'), ('42', '長崎県'), ('43', '熊本県'), ('44', '大分県'), ('45', '宮崎県'), ('46', '鹿児島県'), ('47', '沖縄県') ]

# indexing a element in tuple, in a list 
prefecture_number = [i[0] for i in prefectures]
print(prefecture_number)

prefecture_name = [i[1] for i in prefectures]
print(prefecture_name)


### or ###
for i in prefectures:
    pref_num = i[0]
    pref_name = i[1]
    
    print(pref_num)
    print(pref_name)


