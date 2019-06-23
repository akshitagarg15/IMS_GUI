from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from screens.MdiBackground import MdiArea

from utilities import *
from screens import AddBrandsScreen, ViewBrands, DeleteAndUpdateBrands, AddBrandSubcategoryScreen, ViewBrandSubCategory, \
    DeleteBrandSubCategory, AddItemInfoScreen, DeleteAndUpdateItem, ViewItemInfo, ViewItemById, ViewItemByName, \
    AddStockInfo, Logout, ViewBrandSubCategoryWithOption, DeleteAndUpdateSubCategory, ViewSubCategory, \
    AddSubCategoryScreen, DeleteAndUpdateCategory, ViewCategory, AddCategoryScreen, About, Aboutus
import sys


class UserMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(10,30,1500,1000)
        self.setWindowTitle("Inventory Control System::User")
        newfont=QFont("Bell MT",13,QFont.Bold)

        #Create Menu Bar
        mainMenu=self.menuBar()
        mainMenu.setFont(newfont)
        brandsmenu=mainMenu.addMenu("Brands")
        itemsmenu = mainMenu.addMenu("Items")
        stockmenu = mainMenu.addMenu("Stocks")
        logoutmenu = mainMenu.addMenu("Logout")





        #Actions of Brands
        brandsmenu.setFont(newfont)
        brandAddAction=QAction(QIcon('newbrand.gif'),"Add New Brand",self)
        brandsmenu.addAction(brandAddAction)
        brandAddAction.triggered.connect(self.AddBrand)

        brandViewAction=QAction(QIcon("view.gif"),"View Brand Info",self)
        brandsmenu.addAction(brandViewAction)
        brandViewAction.triggered.connect(self.ViewBrand)

        brandDelUpAction=QAction(QIcon("deledit.gif"),"Delete/Update Brand Info",self)
        brandsmenu.addAction(brandDelUpAction)
        brandDelUpAction.triggered.connect(self.DelUpBrand)



        brandSubCatMenu=brandsmenu.addMenu(QIcon("list(2)"),"Brands SubCategory Operations")

        brandSubCatMenu.setFont(newfont)
        SubCatAddAction=QAction(QIcon('edit.gif'),"Add BrandSubCategory",self)
        brandSubCatMenu.addAction(SubCatAddAction)
        SubCatAddAction.triggered.connect(self.AddBrandSubCat)

        brandsubcatViewMenu=brandSubCatMenu.addMenu(QIcon('list.png'),"View SubCategory Operations")
        brandsubcatViewMenu.setFont(newfont)
        BrandSubCatViewAction = QAction(QIcon('view.gif'),"View Brand-SubCategory Details", self)
        brandsubcatViewMenu.addAction(BrandSubCatViewAction)
        BrandSubCatViewAction.triggered.connect(self.ViewBrandSubCat)

        brandsubcatViewListAction = QAction(QIcon("piclist.gif"),"Brand/Subcategory List", self)
        brandsubcatViewMenu.addAction(brandsubcatViewListAction)
        brandsubcatViewListAction.triggered.connect(self.ListBrandSubCat)

        SubCatDelAction = QAction(QIcon("deledit.gif"),"Delete BrandSubCategory Details", self)
        brandSubCatMenu.addAction(SubCatDelAction)
        SubCatDelAction.triggered.connect(self.DelBrandSubCat)

        #Actions of Items
        itemsmenu.setFont(newfont)
        itemAddAction=QAction(QIcon('pic23.gif'),"Add New Item",self)
        itemsmenu.addAction(itemAddAction)
        itemAddAction.triggered.connect(self.AddItem)

        itemviewMenu = itemsmenu.addMenu(QIcon('list.png'),"View Item Details")
        itemviewMenu.setFont(newfont)
        itemViewAllAction = QAction(QIcon("viewpic.png"),"View All Item Details", self)
        itemviewMenu.addAction(itemViewAllAction)
        itemViewAllAction.triggered.connect(self.ViewAllItems)

        itemViewIdAction = QAction(QIcon("pic18.gif"),"View By ID", self)
        itemviewMenu.addAction(itemViewIdAction)
        itemViewIdAction.triggered.connect(self.ViewIdItem)

        itemViewNameAction = QAction(QIcon("pic5.gif"),"View By Name", self)
        itemviewMenu.addAction(itemViewNameAction)
        itemViewNameAction.triggered.connect(self.ViewNameItem)

        itemDelUpAction=QAction(QIcon("deledit.gif"),"Delete/Update New Item",self)
        itemsmenu.addAction(itemDelUpAction)
        itemDelUpAction.triggered.connect(self.DelUpItem)

        categoryMenu = itemsmenu.addMenu(QIcon("list(2).png"), "Category Operations")
        categoryMenu.setFont(newfont)
        categoryAddAction = QAction(QIcon('newitem.gif'), "Add New Category", self)
        categoryMenu.addAction(categoryAddAction)
        categoryAddAction.triggered.connect(self.AddCategory)

        categoryViewAction = QAction(QIcon("view.gif"), "View Category Info", self)
        categoryMenu.addAction(categoryViewAction)
        categoryViewAction.triggered.connect(self.ViewCategory)

        categoryDelUpAction = QAction(QIcon("deledit.gif"), "Delete/Update Category Info", self)
        categoryMenu.addAction(categoryDelUpAction)
        categoryDelUpAction.triggered.connect(self.DelAndUpdateCategory)

        subcategoryMenu = itemsmenu.addMenu(QIcon("list(2).png"), "SubCategory Operations")
        subcategoryMenu.setFont(newfont)
        subcategoryAddAction = QAction(QIcon('pic17.gif'), "Add New Subcategory", self)
        subcategoryMenu.addAction(subcategoryAddAction)
        subcategoryAddAction.triggered.connect(self.AddSubCategory)

        subcategoryViewAction = QAction(QIcon("view.gif"), "View Subcategory Info", self)
        subcategoryMenu.addAction(subcategoryViewAction)
        subcategoryViewAction.triggered.connect(self.ViewSubCategory)

        subcategoryDelUpAction = QAction(QIcon("deledit.gif"), "Delete/Update Subcategory Details", self)
        subcategoryMenu.addAction(subcategoryDelUpAction)
        subcategoryDelUpAction.triggered.connect(self.DelAndUpdateSubCategory)

        #Actions Of Stock
        stockmenu.setFont(newfont)
        stockAddAction=QAction(QIcon("stock.gif"),"Manage Stock",self)
        stockmenu.addAction(stockAddAction)
        stockAddAction.triggered.connect(self.UpdateStock)

        # Actions OF  Logout
        logoutmenu.setFont(newfont)
        logoutmenu.setFont(newfont)
        aboutAction = QAction(QIcon("care.png"),"About", self)
        logoutmenu.addAction(aboutAction)
        aboutAction.triggered.connect(self.About)

        exitAction = QAction(QIcon("out.gif"),"Exit", self)
        exitAction.setShortcut('ctrl+x')
        logoutmenu.addAction(exitAction)
        exitAction.triggered.connect(self.Logout)


        self.mdi = MdiArea()
        self.setCentralWidget(self.mdi)
        #self.show()

    #Connections of Brand
    def AddBrand(self):
        window = AddBrandsScreen.AddBrandsScreen()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewBrand(self):
        window = ViewBrands.ViewBrands()
        self.mdi.addSubWindow(window)
        window.show()

    def DelUpBrand(self):
        window = DeleteAndUpdateBrands.DeleteAndUpdateBrands()
        self.mdi.addSubWindow(window)
        window.show()
    #Connections of BrandSubCategory
    def AddBrandSubCat(self):
        window = AddBrandSubcategoryScreen.AddBrandSubcategoryScreen()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewBrandSubCat(self):
        window = ViewBrandSubCategory.ViewBrandSubCategory()
        self.mdi.addSubWindow(window)
        window.show()

    def ListBrandSubCat(self):
        window=ViewBrandSubCategoryWithOption.ViewBrandSubCategoryWithOption()
        self.mdi.addSubWindow(window)
        window.show()

    def DelBrandSubCat(self):
        window = DeleteBrandSubCategory.DeleteBrandSubCategory()
        self.mdi.addSubWindow(window)
        window.show()
    #Connections of Items
    def AddItem(self):
        window=AddItemInfoScreen.AddItemInfoScreen()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewAllItems(self):
        window=ViewItemInfo.ViewItemInfo()
        self.mdi.addSubWindow(window)
        window.show()
    def ViewIdItem(self):
        window=ViewItemById.ViewItemById()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewNameItem(self):
        window = ViewItemByName.ViewItemByName()
        self.mdi.addSubWindow(window)
        window.show()

    def DelUpItem(self):
        window=DeleteAndUpdateItem.DeleteAndUpdateItem()
        self.mdi.addSubWindow(window)
        window.show()

    def AddCategory(self):
        window = AddCategoryScreen.AddCategoryScreen()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewCategory(self):
        window = ViewCategory.ViewCategory()
        self.mdi.addSubWindow(window)
        window.show()

    def DelAndUpdateCategory(self):
        window = DeleteAndUpdateCategory.DeleteAndUpdateCategory()
        self.mdi.addSubWindow(window)
        window.show()

    def AddSubCategory(self):
        window = AddSubCategoryScreen.AddSubCategoryScreen()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewSubCategory(self):
        window = ViewSubCategory.ViewSubCategory()
        self.mdi.addSubWindow(window)
        window.show()

    def DelAndUpdateSubCategory(self):
        window = DeleteAndUpdateSubCategory.DeleteAndUpdateSubCategory()
        self.mdi.addSubWindow(window)
        window.show()

    #Connections Of Stock
    def UpdateStock(self):
        window=AddStockInfo.AddStockInfo()
        self.mdi.addSubWindow(window)
        window.show()
    #Connections Of Logout
    def About(self):
        #window=Aboutus.Aboutus()
        #self.mdi.addSubWindow(window)
        message = "Inventory Management System\n\nVersion: 1.0.0.0\nDeveloped By: Akshita Garg\n"
        message += "Email: akshitagarg15@gmail.com"
        ShowMessageDialog(self,message)
        #window.show()

    def Logout(self):
        res = ShowConfirmation(self)
        if res == QMessageBox.Yes:
            sys.exit(True)


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=UserMainWindow()
    sys.exit(app.exec_())