import json
# import re
#
# sum = 0
# i = 0
# while i < 10:
#     i += 1
#     if i % 2:
#         continue
#     if i % 4:
#         sum += 1
# print(sum)
#
#
# class A:
#     items = []
#
#     def __len__(self):
#         return len(self.items)
#
#
# ob = A()
# ob.items.append(True)
#
# ob2 = A()
# print(len(ob2))
#
# a = "linear-gradient(rgb(102, 102, 102) 0%, rgb(77, 77, 77) 100%)"
# result = re.findall("rgb{1}[(\d]\d{3}, \d{3}, \d{3}[)\d]", a)
# print(str(result).strip('[]'))
#
# b = "Last Sync: 05/16/2019 @ 07:45 AM (1h)"
# result_b = re.findall("\d+/\d+/\d+|\d+:\d+", b)
# print(" ".join(result_b))
#
#
# def test_method(online_orders=True):
#     allowed_amount_of_tries = 10
#     amount_of_tries = 0
#
#     while True:
#         if amount_of_tries > allowed_amount_of_tries:
#             print("amount_of_tries > allowed_amount_of_tries")
#             return
#         site_status = False
#         if site_status is online_orders:
#             return site_status
#         amount_of_tries += 1
#
#
# a = test_method()
# print(a)
#
# for i in range(5):
#     print(i)
#
# n = 6000201001525771
# s = "xxxxxxxxxxxx{}".format(str(n)[-4:])
# print(s)

# from functools import wraps
# from time import time
#
#
# def measure(func):
#     @wraps(func)
#     def _time_it(*args, **kwargs):
#         start = int(round(time() * 1000))
#         try:
#             return func(*args, **kwargs)
#         finally:
#             end_ = int(round(time() * 1000)) - start
#             print(f"Total execution time: {end_ if end_ > 0 else 0} ms")
#
#     return _time_it
#
#
# @measure
# def hello():
#     print('hello world')
#
#
# hello()

# c = [5, 1]
# d = c
# d.append(10)
# print(c, d)
# print(id(c), id(d))
#
# # [5, 1, 10] [5, 1, 10]#
# # 4318282208 4318282208
#
#
# a = 4
# b = a
# b = a + 4
# print(a, b)
# print(id(a), id(b))
#
# # 4 8
# # 4316613504 4316613632
#
# ssr = {'ssr': {'name': 'SimpleServiceRegistry', 'description': 'Simple Service Registry', 'key': 'ssr', 'url': 'https://ssr.xenial.com'}, 'portal': {'name': 'xenial Portal', 'description': 'Identity/Auth API', 'key': 'portal', 'url': 'https://qa-xprtbackend.xenial.com'}, 'da': {'name': 'DataMapper', 'description': 'Legacy Data Mapper API', 'key': 'da', 'url': 'https://qa-mapper.xenial.com'}, 'dm': {'name': 'DataManagement', 'description': 'Data Management API', 'key': 'dm', 'url': 'https://qa-dmbackend.xenial.com'}, 'pl': {'name': 'Pipeline', 'description': 'Pipeline API', 'key': 'pl', 'url': 'https://qa-pipeline.xenial.com'}, 'tax': {'name': 'Taxes', 'description': 'Tax Calculation API', 'key': 'tax', 'url': 'https://qa-xenial.xenial.com/tax/api'}, 'dsc': {'name': 'Discounts', 'description': 'Discounts API', 'key': 'dsc', 'url': 'https://qa-xenial.xenial.com/dsc/api'}, 'mo': {'name': 'Mobile Ordering', 'description': 'Mobile Ordering API', 'key': 'mo', 'url': 'https://qa-xooapi.xenial.com'}, 'boh_core': {'name': 'Backoffice Core', 'description': 'Backoffice Core API', 'key': 'boh_core', 'url': 'https://qa-backoffice-api.xenial.com'}, 'boh_day': {'name': 'Daybook', 'description': 'Daybook API', 'key': 'boh_day', 'url': 'https://qa-daybookbackend.xenial.com/api'}, 'boh_inv': {'name': 'Inventory', 'description': 'Inventory API', 'key': 'boh_inv', 'url': 'https://qa-inventorybackend.xenial.com'}, 'weather': {'name': 'Weather', 'description': 'Weather API', 'key': 'weather', 'url': 'https://weather.heartlandcommerce.com/prod/heartland-commerce-weather'}, 'boh_for': {'name': 'Forecast', 'description': 'Forecast API', 'key': 'boh_for', 'url': 'https://qa-forecastbackend.xenial.com'}, 'portal_ui': {'name': 'Portal UI', 'description': 'Portal UI', 'key': 'portal_ui', 'url': 'https://qa-xprt.xenial.com'}, 'drawer': {'name': 'Drawer API', 'description': 'DrawerAPI', 'key': 'drawer', 'url': 'https://qa-drawer.xenial.com'}, 'pl_logs': {'name': 'Pipeline Logs', 'description': 'Pipeline Logs API', 'key': 'pl_logs', 'url': 'https://qa-logs.xenial.com'}, 'comercia_api': {'name': 'Pos comercia API', 'description': 'Pos comercia API', 'key': 'comercia_api', 'url': 'https://qa-xprtwrapper.xenial.com'}, 'xcs': {'name': 'Xenial Communication Service', 'description': 'Xenial Communication Service', 'key': 'xcs', 'url': 'https://qa-xcs.xenial.com'}, 'dm_ui': {'name': 'DataManagement UI', 'description': 'Data Management UI', 'key': 'dm_ui', 'url': 'https://qa-dm.xenial.com'}, 'deposit': {'name': 'DepositAPI', 'description': 'Deposit API', 'key': 'deposit', 'url': 'https://qa-deposit.xenial.com'}, 'boh_core_ui': {'name': 'Backoffice Core UI', 'description': 'Backoffice Core IO', 'key': 'boh_core_ui', 'url': 'https://qa-backoffice.xenial.com/#'}, 'order': {'name': 'Order API', 'description': 'Order API', 'key': 'order', 'url': 'https://qa-order.xenial.com'}, 'XLRUI': {'name': 'LogReaderUI', 'description': 'Log Reader UI', 'key': 'XLRUI', 'url': 'https://qa-log-reader.xenial.com'}, 'XLR': {'name': 'LogReaderAPI', 'description': 'Log Reader API', 'key': 'XLR', 'url': 'https://qa-log-readerbackend.xenial.com'}, 'xoo': {'name': 'Xenial Online Ordering Integrator', 'description': 'Xenial Online Ordering Ecosystem Integration Server', 'key': 'xoo', 'url': 'https://qa-xoobackend.xenial.com'}, 'xoo-ui': {'name': 'Xenial Online Ordering', 'description': 'Xenial Online Ordering Clientele User Interface', 'key': 'xoo-ui', 'url': 'https://qa-xoo.xenial.com'}, 'xenial-pipeline-worker': {'name': 'Xenial Pipeline Worker', 'description': 'Xenial Pipeline Worker', 'key': 'xenial-pipeline-worker', 'url': 'https://qa-pipeline-worker.xenial.com'}, 'timeclock-kiosk-ui': {'name': 'Timeclock Kiosk UI', 'description': 'Timeclock Kiosk UI', 'key': 'timeclock-kiosk-ui', 'url': 'https://qa-timeclock.xenial.com'}, 'boh_day_ui': {'name': 'Daybook UI', 'description': 'Daybook UI', 'key': 'boh_day_ui', 'url': 'https://qa-daybook.xenial.com'}, 'boh_for_ui': {'name': 'Forecast UI', 'description': 'Forecast UI', 'key': 'boh_for_ui', 'url': 'https://qa-forecast.xenial.com'}, 'boh_inv_ui': {'name': 'Inventory UI', 'description': 'Inventory UI', 'key': 'boh_inv_ui', 'url': 'https://qa-inventory.xenial.com'}, 'atrl_api': {'name': 'Xenial Audit Trail API', 'description': 'Audit Trail API', 'key': 'atrl_api', 'url': 'https://qa-audit-trail-backend.xenial.com'}, 'crm_api': {'name': 'Xenial CRM REST-API', 'description': 'CRM API', 'key': 'crm_api', 'url': 'https://stg-api.beanstalkdata.com'}, 'crm_app': {'name': 'Xenial CRM APP', 'description': 'CRM APP', 'key': 'crm_app', 'url': 'https://stg-app.beanstalkdata.com'}, 'reporting_ui': {'name': 'Reporting UI', 'description': 'Reporting UI', 'key': 'reporting_ui', 'url': 'https://qa-reports.xenial.com'}, 'reporting_api': {'name': 'Reporting Api', 'description': 'Reporting Api', 'key': 'reporting_api', 'url': 'https://qa-reportsbackend.xenial.com'}, 'ol': {'name': 'Onboarding Legacy', 'description': 'Onboarding Legacy API', 'key': 'ol', 'url': 'https://qa-ol-history.xenial.com'}, 'olui': {'name': 'Onboarding Legacy UI', 'description': 'Onboarding Legacy UI', 'key': 'olui', 'url': 'https://qa-ol-ui.xenial.com'}, 'xmm-ui': {'name': 'XMM Admin Console', 'description': 'XMM Admin Console', 'key': 'xmm-ui', 'url': 'https://dev-mobilemanager.xenial.com'}, 'xmm-api': {'name': 'XMM API', 'description': 'XMM API', 'key': 'xmm-api', 'url': 'https://xmm-api-dev.xenial.com'}, 'analytics-xp': {'name': 'Analytics XP', 'description': 'Analytics XP', 'key': 'analytics-xp', 'url': 'https://analytics-stage-xp.heartlandcommerce.com'}, 'xenial-checksum': {'name': 'Xenial Checksum', 'description': 'Xenial Checksum', 'key': 'xenial-checksum', 'url': 'https://qa-xenial-checksum.xenial.com'}, 'etl': {'name': 'ETL API', 'description': 'ETL API', 'key': 'etl', 'url': 'https://qa-etl.xenial.com'}, 'boh_staff_ui': {'name': 'Staff UI', 'description': 'Staff UI', 'key': 'boh_staff_ui', 'url': 'https://qa-staff.xenial.com'}, 'dispatcher': {'name': 'Xenial Pipeline Dispatcher', 'description': 'Xenial Pipeline Dispatcher', 'key': 'dispatcher', 'url': 'https://qa-pipeline-dispatcher.xenial.com'}, 'xgs': {'name': 'Xenial Gift Service', 'description': 'Xenial Gift Service', 'key': 'xgs', 'url': 'https://qa-xgs.xenial.com'}, 'whsr': {'name': 'Webhook Subscriber Receiver', 'description': 'Webhook Subscriber Receiver', 'key': 'whsr', 'url': 'https://qa-whsr.xenial.com'}, 'whst': {'name': 'Webhook Subscriber Transformer', 'description': 'Webhook Subscriber Transformer', 'key': 'whst', 'url': 'https://qa-whst.xenial.com'}, 'xad': {'name': 'Xenial Delivery Adapter API', 'description': 'Xenial Delivery Adapter API', 'key': 'xad', 'url': 'https://qa-xad.xenial.com'}, 'xme': {'name': 'Menu Engine', 'description': 'Menu Engine', 'key': 'xme', 'url': 'https://qa-xme.xenial.com'}, 'xmc': {'name': 'Xenial Menu Creator', 'description': 'Xenial Menu Creator', 'key': 'xmc', 'url': 'https://qa-xmc.xenial.com'}, 'xmp': {'name': 'Xenial Menu Publisher', 'description': 'Xenial Menu Publisher', 'key': 'xmp', 'url': 'https://qa-xmp.xenial.com'}}
# xgs = ssr.get('xgs')
# xgs.update({'url': ''})
#
#
# print(xgs)
# print(ssr)

# a = [3, 1]
# arr = sorted(a)
#
# print("{}/{}".format(str(arr[0]), str(arr[1])))

#
# receipt = [{'itemName': '_ART_senioritempattern', 'itemQuantity': '1', 'itemPrice': '$1.50'},
#            {'itemName': '_ART_seriouseffectyes', 'itemQuantity': '1', 'itemPrice': '$3.00'}]
#
# receipt = [{'itemName': 'FLATE_WHITE_PRODUCTissu...', 'itemQuantity': '1', 'itemPrice': '$2.00'},
#            {'itemName': 'FLATE_WHITE_PRODUCTissu...', 'itemQuantity': '1', 'itemPrice': '$2.00'},
#            {'itemName': '', 'itemQuantity': '1', 'itemPrice': '$1.00'}]
#
#
# var = str(6000201001525666)
# print(var[-4:])

# json = {'calculations': {'gross_sales': {'total': '5.41'}, 'discount_total': {'total': '0.00', 'quantity': '0'}, 'liability_items': {'total': '0.00', 'quantity': '0'}, 'post_payment_voids_total': {'total': '5.41', 'quantity': '1'}, 'refund_total': {'total': '0.00'}, 'tax_total': {'total': '0.00'}, 'voided_orders_total': {'total': '0.00', 'quantity': '0.00'}, 'net_sales': {'total': '0.00', 'quantity': '0'}}, 'payments': {'payments_total': '0.00', 'payments_quantity': '0', 'pay_type_totals': []}, 'reconciliation': {'drawers': {'count_total': '0.00', 'expected_total': '150.00', 'pull_total': '0.00', 'variance': '-150.00'}, 'deposits': {'actual_total': '0.00', 'expected_total': '0.00', 'variance': '0.00'}}, 'destinations': {'destinations_total': '0.00', 'destinations_quantity': '0', 'destinations_totals': []}, 'discounts': {'discounts_total': '0.00', 'discounts_quantity': '0', 'discounts_totals': []}, 'day_parts': {'day_parts_total': '0.00', 'day_parts_quantity': '0', 'day_parts_totals': []}, 'liability_items': {'liability_items_total': '0.00', 'liability_items_quantity': '0', 'liability_items_promotions': '0.00', 'liability_items_totals': []}, 'donations': {'donations_total': '0.00', 'donations_quantity': '0', 'donations_totals': []}, 'order_sources': {'order_sources_total': '0.00', 'order_sources_quantity': '0', 'order_sources_totals': []}, 'taxes': {'taxes_total': '0.00', 'tax_rate_totals': [], 'tax_class_totals': []}, 'tips': {'tips_total': '0.00'}}
#
json_receipt = [{'discounts': [{'itemName': '_ART_littleboxturn', 'itemPrice': '$(1.00)'}], 'itemName': '_ART_claimwalkthey', 'itemPrice': '$2.00', 'itemQuantity': '1'}, {'itemName': '_ART_readonlocal', 'itemPrice': '$1.00', 'itemQuantity': '1'}]
value = json.dumps(json_receipt )
print(value)

# m = "= Gross Sales"
# n = m[2:]
# print(n)

