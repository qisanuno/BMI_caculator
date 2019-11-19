身高 = input('請輸入身高CM:')
身高 = int(身高)
體重 = input('請輸入體重Kg:')
體重 = int(體重)
BMI = 體重 / ( ( 身高 / 100) * (身高 / 100) )
BMI = int(BMI)
print('這是你的BMI值:', BMI)

if BMI < 18.5:
	print('您的體重屬於，體重過輕')
elif BMI >= 18.5 and BMI < 24:
	print('您的體重屬於，正常範圍')
elif BMI >= 24 and BMI < 27:
	print('您的體重屬於，過重')
elif BMI >= 27 and BMI < 30:
	print('您的體重屬於，輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('您的體重屬於，中度肥胖')
else:
	print('您的體重屬於，重度肥胖')