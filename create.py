import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active


sheet ['A1'] = "ID"
sheet ['B1'] = "customer name"
sheet['C1'] = "product"
sheet['D1'] = "quantity"
sheet['E1'] = "price"
sheet['F1'] = "total"

workbook.save("ordersDB.xlsx")