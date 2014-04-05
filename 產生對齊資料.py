import os

class 產生對齊資料:
	plain2snt = '/usr/local/giza-pp-v1.0.7/GIZA++-v2/plain2snt.out'
	snt2cooc = '/usr/local/giza-pp-v1.0.7/GIZA++-v2/snt2cooc.out'
	mkcls = '/usr/local/giza-pp-v1.0.7/mkcls-v2/mkcls'
	gizapp = '/usr/local/giza-pp-v1.0.7/GIZA++-v2/GIZA++'
	文本 = '{0}.txt'
	詞數統計 = '{0}.vcb'
	平行語料統計 = '{0}_{1}.snt'
	對齊資料 = '{0}_{1}.cooc'
	詞性 = '{0}.vcb.classes'
	對齊結果 = '{0}_{1}'
	def 產生(self, 來源語料, 目標語料, 工作目錄 = None,
			愛轉giza = True, 愛產生對齊詞 = True,
			愛分詞類 = True, 愛對齊句 = True):
		來源文本 = self.文本.format(來源語料)
		目標文本 = self.文本.format(目標語料)
		轉giza格式 = '{0} {1} {2}'
		if 愛轉giza:
			os.system(轉giza格式.format(self.plain2snt, 來源文本, 目標文本))

		來源詞數統計 = self.詞數統計.format(來源語料)
		目標詞數統計 = self.詞數統計.format(目標語料)
		來源平行語料統計 = self.平行語料統計.format(來源語料, 目標語料)
		目標平行語料統計 = self.平行語料統計.format(目標語料, 來源語料)
		來源對齊詞 = self.對齊資料.format(來源語料, 目標語料)
		目標對齊詞 = self.對齊資料.format(目標語料, 來源語料)
		產生對齊詞 = '{0} {1} {2} {3} > {4}'
		if 愛產生對齊詞:
			os.system(產生對齊詞.format(self.snt2cooc,
				來源詞數統計, 目標詞數統計,
				來源平行語料統計, 來源對齊詞))
			os.system(產生對齊詞.format(self.snt2cooc,
				目標詞數統計, 來源詞數統計,
				目標平行語料統計, 目標對齊詞))

		來源詞性 = self.詞性.format(來源語料)
		目標詞性 = self.詞性.format(目標語料)
		分詞類 = '{0} -p{1} -V{2} opt'
		if 愛分詞類:
			os.system(分詞類.format(self.mkcls,
				來源文本, 來源詞性))
			os.system(分詞類.format(self.mkcls,
				目標文本, 目標詞性))

		來源對齊結果 = self.對齊結果.format(來源語料, 目標語料)
		目標對齊結果 = self.對齊結果.format(目標語料, 來源語料)
		產生對齊句 = '{0} -S {1} -T {2} -C {3} -CoocurrenceFile {4} -O {5}'
		if 愛對齊句:
			os.system(產生對齊句.format(self.gizapp,
				來源詞數統計, 目標詞數統計,
				來源平行語料統計, 來源對齊詞, 來源對齊結果))
			os.system(產生對齊句.format(self.gizapp,
				目標詞數統計, 來源詞數統計,
				目標平行語料統計, 目標對齊詞, 目標對齊結果))
# 			print(產生對齊句.format(self.gizapp,
# 				目標詞數統計, 來源詞數統計,
# 				目標平行語料統計, 目標對齊詞, 目標對齊結果))

if __name__ == '__main__':
	對齊資料 = 產生對齊資料()
	對齊資料.產生('訓.國語字', '訓.閩南語音',
		愛轉giza = True, 愛產生對齊詞 = True,
		愛分詞類 = True, 愛對齊句 = True)
