import os,sys
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),"../../python"))
#print os.path.join(os.path.dirname(os.path.abspath(__file__)),"../../python")
import chargebee
from chargebee.main import Environment
Environment.chargebee_domain="localcb.in:8080"
Environment.protocol = "http"
chargebee.ChargeBee.verify_ca_certs=False

##Copy code from api docs
chargebee.configure("test___dev__2BgdqjK9jMcXc9pzFlunAhcd9vcd2irK5W","mannar-test")


def customer_retrieve():
   #result = chargebee.Customer.retrieve("1sGeZ2FOvI0H2E4y")
   result = chargebee.Customer.retrieve("1sGeZ2FOvHb5cF1I")
   print result.customer
   print result.card
   print result.customer.payment_method
   print result.customer.payment_method.status
   print result.customer.payment_method.reference_id
   print result.customer.payment_method.type


def update_payment_method_customer():
	result = chargebee.result = chargebee.Customer.update_payment_method("__dev__KyVq6pPB30WON1", {
    	"payment_method" : {
        "type" : "paypal_express_checkout", 
        "reference_id" : "B-0VP263300J9780"
    	}})
        print result.customer.payment_method 

def create_customer():
 result = chargebee.Customer.create({
    "first_name" : "John", 
    "last_name" : "Doe", 
    "email" : "john@test.com",
    "payment_method" : {
        "type" : "amazon_payments",
        "reference_id" : "B-04V710325S436224L"
        }})
 print result

def collect_invoice():
 result = chargebee.Invoice.collect_payment("__demo_inv__6")
 print result

def update_subscription():
 result = chargebee.Subscription.update("future_billing", {
    "plan_id" : "cbee_multiple_site_plan", 
    "payment_method" : {
        "type" : "paypal_express_checkout",
        "reference_id" : "B-04V710325S436224L"
      }})
 print result


def create_subscription():
 result = chargebee.Subscription.create({
    "plan_id" : "cbee_multiple_site_plan", 
    "customer" : {
        "email" : "john@user.com", 
        "first_name" : "John", 
        "last_name" : "Doe", 
        "phone" : "+1-949-999-9999"
    },
     "payment_method" : {
        "type" : "card",
        "reference_id" : "B-04V710325S436224L"
      }})
 print result

def retrieve_card():
  result = chargebee.Card.retrieve("1sGeZ2FOvI0H2E4y")
  #result = chargebee.Card.retrieve("1sGeZ2FOvHb5cF1I")
  card = result.card
  print result.card


def update_card_amazon():
   result = chargebee.Card.update_card_for_customer("1sGeZ2FOvHb5cF1I", {
     "gateway" : "chargebee", 
     "first_name" : "Richard", 
     "last_name" : "Fox", 
     "number" : "4012888888881881", 
     "expiry_month" : 10, 
     "expiry_year" : 2015, 
     "cvv" : "999"
   }) 
   print result.customer
   print result.card
   print result.customer.payment_method
   print result.customer.payment_method.reference_id
   print result.customer.payment_method.type


def amazon_txn():
 result = chargebee.Transaction.retrieve("txn_1sGeZ2FOvHzDwG4Y")
 #result = chargebee.Transaction.retrieve("txn_1sGeZ2FOvI530V5R")
 print result
 print result.transaction
 print result.transaction.payment_method 


def retrieve_events():
 result = chargebee.Event.retrieve("ev___dev__KyVqiWPMvuj0qC")
 event = result.event
 print event
 if event.webhooks is not None:
    for w in event.webhooks:
        print w.webhook_status
        print w.id
 print event.user

def list_events():
 result = chargebee.Event.list()
 for entry in result:
    event = entry.event
    print event
    print event.id
    print event.webhook_status
    print event.webhook_failure_reason
    print event.user
    print type(event.webhooks) is dict
    if event.webhooks is not None:
       for w in event.webhooks:
          print w.webhook_status 
          print w.id
    print "==========="

list_events()
#retrieve_events()
#collect_invoice()
#create_customer()
#create_subscription()
#update_subscription()
#amazon_txn()
#retrieve_card()
#update_card_amazon()
#customer_retrieve()
#update_payment_method_customer()