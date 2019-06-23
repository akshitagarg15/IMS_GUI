from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from screens.MdiBackground import MdiArea
from utilities import *
from screens import AddBrandsScreen, ViewBrands, DeleteAndUpdateBrands, AddBrandSubcategoryScreen, ViewBrandSubCategory, \
    DeleteBrandSubCategory, DeleteAndUpdateSubCategory, AddItemInfoScreen, ViewItemInfo, ViewItemById, ViewItemByName, \
    DeleteAndUpdateItem, AddCategoryScreen, ViewCategory, DeleteAndUpdateCategory, AddSubCategoryScreen, \
    ViewSubCategory, AddStockInfo, AddSupplierScreen, ViewSupplier, ViewSupplierByName, ViewSupplierByContact, \
    ViewSupplierByGst, ViewSupplierById, DeleteAndUpdateSupplier, AddSupplierBrandInfo, ViewSupplierBrandInfo, \
    DeleteSupplierBrandInfo, AddCustomers, ViewCustomerInfo, ViewCustomerById, ViewCustomerByContact, \
    DeleteAndUpdateCustomer, Logout, ViewBrandSubCategoryWithOption, ViewSupplierBrandList, AddEmployeeInfo, \
    ViewEmployeeInfo, SettingsReplica, About, Aboutus, AddEmpPhoto
from screens import BillScreen
import sys

class AdminMainWindow(QMainWindow):
    def __init__(self,uname=None):
        super().__init__()
        self.username=uname

        self.setGeometry(10,30,1500,1000)
        self.setWindowTitle("Inventory Management System::Admin")
        newfont=QFont("Bell MT",13,QFont.Bold)


        #Providing Customize Color Button in BackGround
        button=QPushButton("OpenColorDialog",self)
        button.setToolTip("Opens Color Dialog")
        button.move(50,50)
        button.clicked.connect(self.OnClickFunc)

        #Create Menu Bar
        mainMenu=self.menuBar()
        mainMenu.setFont(newfont)
        brandsmenu=mainMenu.addMenu("Brands")
        brandsmenu.setFont(newfont)
        itemmenu=mainMenu.addMenu("Items")
        stockmenu=mainMenu.addMenu("Stocks")
        suppliermenu=mainMenu.addMenu("Suppliers")
        employeemenu=mainMenu.addMenu("Employees")
        customermenu=mainMenu.addMenu("Customers")
        billmenu=mainMenu.addMenu("Billing")
        logoutmenu=mainMenu.addMenu("Logout")

        #Actions Of Brands

        brandAddAction=QAction(QIcon('newbrand.gif'),"Add New Brand",self)

        brandsmenu.addAction(brandAddAction)
        brandAddAction.setStatusTip("Add New brand details")
        brandAddAction.triggered.connect(self.AddBrand)

        brandViewAction = QAction(QIcon("view.gif"),"View Brand Info", self)
        brandsmenu.addAction(brandViewAction)
        brandViewAction.triggered.connect(self.ViewBrand)

        brandDelUpAction=QAction(QIcon("deledit.gif"),"Delete/Update Brand Info",self)
        brandsmenu.addAction(brandDelUpAction)
        brandDelUpAction.triggered.connect(self.DelAndUpdateBrand)




        brandsubcatMenu=brandsmenu.addMenu(QIcon("list(2)"),"Brand SubCategory Operations")
        brandsubcatMenu.setFont(newfont)
        brandsubcatAddAction=QAction(QIcon('edit.gif'),"Add New BrandSubCategory",self)
        brandsubcatMenu.addAction(brandsubcatAddAction)
        brandsubcatAddAction.triggered.connect(self.AddBrandSubCat)


        brandsubcatViewMenu = brandsubcatMenu.addMenu(QIcon('list.png'),"View BrandSubCategory Info")
        brandsubcatViewMenu.setFont(newfont)
        brandsubcatViewAction=QAction(QIcon('view.gif'),"View Brand-SubCategory All Details",self)
        brandsubcatViewMenu.addAction(brandsubcatViewAction)
        brandsubcatViewAction.triggered.connect(self.ViewBrandSubCat)

        #brandsubcatlistViewMenu= brandsubcatViewMenu.addMenu("View Brand/SubCategory List")
        brandsubcatViewListAction=QAction(QIcon("piclist.gif"),"Brand/Subcategory List",self)
        brandsubcatViewMenu.addAction(brandsubcatViewListAction)
        brandsubcatViewListAction.triggered.connect(self.ListBrandSubCat)

        brandsubcatDelUpAction = QAction(QIcon("deledit.gif"),"Delete BrandSubCategory Details", self)
        brandsubcatMenu.addAction(brandsubcatDelUpAction)
        brandsubcatDelUpAction.triggered.connect(self.DelBrandSubCat)

        #Actions Of Items
        itemmenu.setFont(newfont)
        itemAddAction=QAction(QIcon('pic23.gif'),"Add New Item",self)
        itemmenu.addAction(itemAddAction)
        itemAddAction.triggered.connect(self.AddItem)

        itemviewMenu=itemmenu.addMenu(QIcon('list.png'),"View Item Details")
        itemviewMenu.setFont(newfont)
        itemViewAllAction=QAction(QIcon("viewpic.png"),"View All Item Details",self)
        itemviewMenu.addAction(itemViewAllAction)
        itemViewAllAction.triggered.connect(self.ViewAllItems)

        itemViewIdAction = QAction(QIcon("pic18.gif"),"View By ID", self)
        itemviewMenu.addAction(itemViewIdAction)
        itemViewIdAction.triggered.connect(self.ViewIdItem)

        itemViewNameAction = QAction(QIcon("pic5.gif"),"View By Name", self)
        itemviewMenu.addAction(itemViewNameAction)
        itemViewNameAction.triggered.connect(self.ViewNameItem)

        itemDelUpAction = QAction(QIcon("deledit.gif"),"Delete/Update Item Details", self)
        itemmenu.addAction(itemDelUpAction)
        itemDelUpAction.triggered.connect(self.DelAndUpdateItem)

        categoryMenu=itemmenu.addMenu(QIcon("list(2).png"),"Category Operations")
        categoryMenu.setFont(newfont)
        categoryAddAction=QAction(QIcon('newitem.gif'),"Add New Category",self)
        categoryMenu.addAction(categoryAddAction)
        categoryAddAction.triggered.connect(self.AddCategory)

        categoryViewAction = QAction(QIcon("view.gif"), "View Category Info", self)
        categoryMenu.addAction(categoryViewAction)
        categoryViewAction.triggered.connect(self.ViewCategory)

        categoryDelUpAction = QAction(QIcon("deledit.gif"), "Delete/Update Category Info", self)
        categoryMenu.addAction(categoryDelUpAction)
        categoryDelUpAction.triggered.connect(self.DelAndUpdateCategory)

        subcategoryMenu=itemmenu.addMenu(QIcon("list(2).png"),"SubCategory Operations")
        subcategoryMenu.setFont(newfont)
        subcategoryAddAction=QAction(QIcon('pic17.gif'),"Add New Subcategory",self)
        subcategoryMenu.addAction(subcategoryAddAction)
        subcategoryAddAction.triggered.connect(self.AddSubCategory)

        subcategoryViewAction = QAction(QIcon("view.gif"),"View Subcategory Info", self)
        subcategoryMenu.addAction(subcategoryViewAction)
        subcategoryViewAction.triggered.connect(self.ViewSubCategory)

        subcategoryDelUpAction = QAction(QIcon("deledit.gif"),"Delete/Update Subcategory Details", self)
        subcategoryMenu.addAction(subcategoryDelUpAction)
        subcategoryDelUpAction.triggered.connect(self.DelAndUpdateSubCategory)

        #Actions of stocks
        stockmenu.setFont(newfont)
        stockAddAction=QAction(QIcon("stock.gif"),"Update Stocks",self)
        stockmenu.addAction(stockAddAction)
        stockAddAction.triggered.connect(self.StockChange)


        #Actions Of Supplier
        suppliermenu.setFont(newfont)
        supplierAddAction=QAction(QIcon('pic15.gif'),"Add New Supplier",self)
        suppliermenu.addAction(supplierAddAction)
        supplierAddAction.triggered.connect(self.AddSupplier)


        supplierViewMenu = suppliermenu.addMenu(QIcon("list.png"),"View Supplier Operations")
        supplierViewMenu.setFont(newfont)
        supplierViewAllAction = QAction(QIcon("view11.gif"),"View ALL Supplier Details", self)
        supplierViewMenu.addAction(supplierViewAllAction)
        supplierViewAllAction.triggered.connect(self.ViewAllSupplier)

        supplierViewByIdAction = QAction(QIcon("view9.gif"),"View By Id", self)
        supplierViewMenu.addAction(supplierViewByIdAction)
        supplierViewByIdAction.triggered.connect(self.ViewByIdSupplier)

        supplierViewByNameAction = QAction(QIcon("pic5.gif"),"View By Name", self)
        supplierViewMenu.addAction(supplierViewByNameAction)
        supplierViewByNameAction.triggered.connect(self.ViewByNameSupplier)

        supplierViewByGSTAction = QAction(QIcon("view12.gif"),"View By GSTno", self)
        supplierViewMenu.addAction(supplierViewByGSTAction)
        supplierViewByGSTAction.triggered.connect(self.ViewByGSTSupplier)

        supplierViewByContactAction = QAction(QIcon("view2.gif"),"View By Contact", self)
        supplierViewMenu.addAction(supplierViewByContactAction)
        supplierViewByContactAction.triggered.connect(self.ViewByContactSupplier)

        supplierDelUpAction = QAction(QIcon("pic25.gif"),"Delete/Update Supplier Details", self)
        suppliermenu.addAction(supplierDelUpAction)
        supplierDelUpAction.triggered.connect(self.DelAndUpdateSupplier)

        supplierbrandMenu=suppliermenu.addMenu(QIcon("list(2).png"),"Supplier Brand Operations")
        supplierbrandMenu.setFont(newfont)
        supplierbrandAddAction=QAction(QIcon("edit.gif"),"Add Supplier Brands",self)
        supplierbrandMenu.addAction(supplierbrandAddAction)
        supplierbrandAddAction.triggered.connect(self.AddSupplierBrand)

        supplierbrandViewMenu=supplierbrandMenu.addMenu(QIcon("list.png"),"Supplier-Brand View Operations")
        supplierbrandViewMenu.setFont(newfont)
        supplierbrandViewAllAction = QAction(QIcon("view.gif"),"View Supplier-Brands Info", self)
        supplierbrandViewMenu.addAction(supplierbrandViewAllAction)
        supplierbrandViewAllAction.triggered.connect(self.ViewAllSupplierBrand)

        supplierbrandListAction = QAction(QIcon("piclist.gif"),"Brand/Supplier List", self)
        supplierbrandViewMenu.addAction(supplierbrandListAction)
        supplierbrandListAction.triggered.connect(self.ViewBrandSupplierList)

        #supplierbrandSupAllAction = QAction("View By Supplier Details", self)
        #supplierbrandViewMenu.addAction(supplierbrandSupAllAction)
        #supplierbrandSupAllAction.triggered.connect(self.ViewSupSupplierBrand)

        supplierbrandDelUpAction = QAction(QIcon("deledit.gif"),"Delete/Update SupplierBrand details", self)
        supplierbrandMenu.addAction(supplierbrandDelUpAction)
        supplierbrandDelUpAction.triggered.connect(self.DelAndUpdateSupplierBrand)

        #Actions Of Employee
        employeemenu.setFont(newfont)
        employeeAddAction=QAction(QIcon("newemployee.gif"),"Add New Emplooyee",self)
        employeemenu.addAction(employeeAddAction)
        employeeAddAction.triggered.connect(self.AddEmployee)

        employeeAddPicAction = QAction(QIcon("newemployee.gif"), "Add Emplooyee Photo", self)
        employeemenu.addAction(employeeAddPicAction)
        employeeAddPicAction.triggered.connect(self.AddEmployeePic)

        employeeViewAllAction = QAction("View Emplooyee Details", self)
        employeemenu.addAction(employeeViewAllAction)
        employeeViewAllAction.triggered.connect(self.ViewEmployee)

        # Actions of Customer
        customermenu.setFont(newfont)

        #customerViewMenu = customermenu.addMenu("View Customer Info")
        #customerViewMenu.setFont(newfont)
        customerViewAllAction = QAction(QIcon("viewpic.png"),"View ALL Customer Info", self)

        customermenu.addAction(customerViewAllAction)
        customerViewAllAction.triggered.connect(self.ViewCustomers)

        customerViewIdAction = QAction(QIcon("view9.gif"),"By Id", self)
        customermenu.addAction(customerViewIdAction)
        customerViewIdAction.triggered.connect(self.ViewByIdCustomers)

        customerViewConAction = QAction(QIcon("view2.gif"),"By Contact ", self)
        customermenu.addAction(customerViewConAction)
        customerViewConAction.triggered.connect(self.ViewByConCustomers)

        #customerDelUpAction = QAction(QIcon("pic6.gif"),"Delete/Update Customer Details", self)
        #customermenu.addAction(customerDelUpAction)
        #customerDelUpAction.triggered.connect(self.DelAndUpdateCustomers)

        #Actions Of Billing
        billAction=QAction(QIcon("pic24.gif"),"Bill Screen",self)
        billmenu.addAction(billAction)
        billmenu.setFont(newfont)
        billAction.triggered.connect(self.BillScreen)

        #Actions OF  Logout
        logoutmenu.setFont(newfont)
        settingAction=QAction(QIcon("settings.png"),"Settings",self)
        logoutmenu.addAction(settingAction)
        settingAction.setShortcut("ctrl+H")
        settingAction.triggered.connect(self.Setting)


        aboutAction = QAction(QIcon("care.png"),"About Us", self)
        logoutmenu.addAction(aboutAction)
        aboutAction.triggered.connect(self.About)

        exitAction=QAction(QIcon("out.gif"),"Exit",self)
        logoutmenu.addAction(exitAction)
        exitAction.setShortcut("ctrl+x")
        exitAction.triggered.connect(self.Logout)

            # LoginAction = QAction("Login Thro", self)
        #logoutmenu.addAction(exitAction)
        #exitAction.triggered.connect(self.Exit)

        self.mdi=MdiArea()
        self.setCentralWidget(self.mdi)

        #self.show()

    @pyqtSlot()
    def OnClickFunc(self):
        self.OpenColorDialog()

    def OpenColorDialog(self):
        color=QColorDialog.getColor()
        if color.isVaild():
            style="background-color::{}".format(color.name())
            self.styleSheet(style)
        #Functions Of All the menu

    def AddBrand(self):
        window = AddBrandsScreen.AddBrandsScreen()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewBrand(self):
        window = ViewBrands.ViewBrands()
        self.mdi.addSubWindow(window)
        window.show()



    def DelAndUpdateBrand(self):
        window = DeleteAndUpdateBrands.DeleteAndUpdateBrands()
        self.mdi.addSubWindow(window)
        window.show()

    def AddBrandSubCat(self):
        try:

            window = AddBrandSubcategoryScreen.AddBrandSubcategoryScreen()
            self.mdi.addSubWindow(window)
            window.show()
            print(2)
        except BaseException as ex:
            print(ex)

    def ViewBrandSubCat(self):
        window = ViewBrandSubCategory.ViewBrandSubCategory()
        self.mdi.addSubWindow(window)
        window.show()

    def ListBrandSubCat(self):
        window=ViewBrandSubCategoryWithOption.ViewBrandSubCategoryWithOption()
        self.mdi.addSubWindow(window)
        window.show()

    def DelBrandSubCat(self):
        try:
            window = DeleteBrandSubCategory.DeleteBrandSubCategory()
            self.mdi.addSubWindow(window)
            window.show()
        except BaseException as ex:
            print(ex)

    def StockChange(self):
        window=AddStockInfo.AddStockInfo()
        self.mdi.addSubWindow(window)
        window.show()

    def AddItem(self):
        window = AddItemInfoScreen.AddItemInfoScreen()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewAllItems(self):
        window = ViewItemInfo.ViewItemInfo()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewIdItem(self):
        window = ViewItemById.ViewItemById()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewNameItem(self):
        window = ViewItemByName.ViewItemByName()
        self.mdi.addSubWindow(window)
        window.show()

    def DelAndUpdateItem(self):
        window = DeleteAndUpdateItem.DeleteAndUpdateItem()
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

    def AddEmployee(self):

        window=AddEmployeeInfo.AddEmployeeInfo()
        self.mdi.addSubWindow(window)
        window.show()

    def AddEmployeePic(self):
        window=AddEmpPhoto.AddEmpPhoto()
        self.mdi.addSubWindow(window)
        window.show()



    def ViewEmployee(self):
        window=ViewEmployeeInfo.ViewEmployeeInfo()
        self.mdi.addSubWindow(window)
        window.show()


    '''def AddCustomers(self):
        window=AddCustomers.AddCustomers()
        self.mdi.addSubWindow(window)
        window.show()'''

    def ViewCustomers(self):
        window=ViewCustomerInfo.ViewCustomerInfo()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewByIdCustomers(self):
        window=ViewCustomerById.ViewCustomerById()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewByConCustomers(self):
        window = ViewCustomerByContact.ViewCustomerByContact()
        self.mdi.addSubWindow(window)
        window.show()

    '''def DelAndUpdateCustomers(self):
        window=DeleteAndUpdateCustomer.DeleteAndUpdateCustomer()
        self.mdi.addSubWindow(window)
        window.show()'''

    def AddSupplier(self):
        window=AddSupplierScreen.AddSupplierScreen()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewAllSupplier(self):
        window=ViewSupplier.ViewSupplier()
        self.mdi.addSubWindow(window)
        window.show()
    def ViewByIdSupplier(self):
        window=ViewSupplierById.ViewSupplierById()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewByNameSupplier(self):
        window=ViewSupplierByName.ViewSupplierByName()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewByGSTSupplier(self):
        window=ViewSupplierByGst.ViewSupplierByGst()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewByContactSupplier(self):
        window=ViewSupplierByContact.ViewSupplierByContact()
        self.mdi.addSubWindow(window)
        window.show()

    def DelAndUpdateSupplier(self):
        window=DeleteAndUpdateSupplier.DeleteAndUpdateSupplier()
        self.mdi.addSubWindow(window)
        window.show()

    def AddSupplierBrand(self):
        window=AddSupplierBrandInfo.AddSupplierBrandInfo()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewAllSupplierBrand(self):
        window=ViewSupplierBrandInfo.ViewSupplierBrandInfo()
        self.mdi.addSubWindow(window)
        window.show()

    def ViewBrandSupplierList(self):
        window = ViewSupplierBrandList.ViewSupplierBrandList()
        self.mdi.addSubWindow(window)
        window.show()

    def DelAndUpdateSupplierBrand(self):
        window=DeleteSupplierBrandInfo.DeleteSupplierBrandInfo()
        self.mdi.addSubWindow(window)
        window.show()

    def Setting(self):
        try:
            window=About.About()
            self.mdi.addSubWindow(window)
            window.showMaximized()
        except BaseException as ex:
            print(ex)

    def BillScreen(self):
        try:

            window=BillScreen.BillScreen(self.username)
            self.mdi.addSubWindow(window)
            window.show()
        except BaseException as ex:
            print(ex)
    def Logout(self):
        res = ShowConfirmation(self)
        if res == QMessageBox.Yes:
            sys.exit(True)
    def About(self):

        message = "Inventory Management System\n\nVersion: 1.0.0.0\nDeveloped By: Akshita Garg\n"
        message += "Email: akshitagarg15@gmail.com"
        ShowMessageDialog(self,message)



if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=AdminMainWindow()
    sys.exit(app.exec_())