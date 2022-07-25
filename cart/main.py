class Cart:
	
	__jumlah = 0
	
	def __init__(self, produk, entity):
		self.produk = produk
		self.entity = entity
  
		Cart.__jumlah += 1

	def tambahProduk(self, jumlah):
		self.jumlah += jumlah

	def hapusProduk(self):
		self.produk = None
		self.jumlah = None

	def tampilkanCart(self):
		print(self.produk, self.jumlah)

keranjangPisang = Cart("Pisang Hijau", 2)
keranjangSemangka = Cart("Semangka Kuning", 3)
KeranjangApel = Cart("Apel Merah", 1)

KeranjangApel.tambahProduk(4)
KeranjangApel.tambahProduk(2)

keranjangSemangka.hapusProduk()

keranjangPisang.tampilkanCart()
keranjangSemangka.tampilkanCart()
KeranjangApel.tampilkanCart()