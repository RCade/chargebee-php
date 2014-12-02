### v1.1.51 (2014-12-02)
* * *

**APIs added**:
A new resource called Order is introduced. This can be used for integrating ChargeBee with any shipping/order management application (like ShipStation). Orders are not automatically generated or updated by ChargeBee currently. They have to be created/updated either via api or merchant web console (a.k.a admin console). An order can be created against an invoice irrespective of the status of the invoice and an invoice can have multiple orders associated with it.
See https://apidocs.chargebee.com/docs/api/orders?lang=java for details.

**API Updates**:
Ability to filter Invoices with paidOnAfter parameter. See https://apidocs.chargebee.com/docs/api/invoices?lang=java#list_invoices.

### v1.1.50 (2014-11-24)
* * *

* Support for Amazon Payments
* Details about customer's payment method is now available as sub resource of Customer.

### v1.1.49 (2014-10-12)
* * *

**APIs Updated**:
* Set auto colection to on/off via "Update a customer" API. See https://apidocs.chargebee.com/docs/api/customers#update_a_customer.

### v1.1.48 (2014-09-16)
* * *

**Error Model**:

New simpler model for error handling has been implemented. Please see https://apidocs.chargebee.com/docs/api?lang=java#error_handling for more details.
The following variables in ApiException have been deprecated.
* code  (Use apiErrorCode instead).
* message (Use getMessage instead).
* httpCode (Use httpStatusCode instead).

**APIs Updated**:

Shipping Address support added to *create subscription for a customer* api call.

### v1.1.47 (2014-08-28)
* * *
* Customer id can be passed to the checkout new subscription operation.

* Added support for affiliate integration to accept affiliate token and the ip address from where the subscription was created. See https://apidocs.chargebee.com/docs/api/subscriptions#create_a_subscription.

### v1.1.46 (2014-08-13)
* * *
Added properties:
* Property has_scheduled_changes added to the Subscription resource to indicate whether there are any pending change scheduled for this Subscription

APIs added:
* Retrieve a subscription with scheduled changes applied. See https://apidocs.chargebee.com/docs/api/subscriptions#retrieve_with_scheduled_changes.
* Remove schedule changes for a subscription. See https://apidocs.chargebee.com/docs/api/subscriptions#remove_scheduled_changes.

APIs updated:
* Ability to pass description for Plans & Addons while Creating & Updating. 

APIs Removed:
* Refund a Transaction - In ChargeBee, the 'refunds' are tracked against the invoice for which they are issued. A payment transaction can be associated with only one invoice now. So Transaction.refund() API is indeed a shortcut for Transaction.associatedInvoice().refund(). 

### v1.1.45 (2014-07-29)
* * *
APIs added:
* Add a one time charged to the subscription which will be added to the invoice generated at the end of the current term. See https://apidocs.chargebee.com/docs/api/subscriptions#add_charge_at_term_end.
* Add a "non-recurring addon" charge to a subscription which will be added to the invoice generated at the end of the current term. See https://apidocs.chargebee.com/docs/api/subscriptions#charge_addon_at_term_end.
*Return an estimate of the amount that will be charged when the subscription renews. See https://apidocs.chargebee.com/docs/api/estimates#subscription_renewal_estimate

APIs updated:
* Now plans supports charge model to specify how the subscription plan charges should be calculated. See https://apidocs.chargebee.com/docs/api/plans#plan_attributes
* Include delayed charges while calculating the Estimate.

### v1.1.44 (2014-06-19)
* * *
APIs added:
* Retrieve invoices for a customer. See https://apidocs.chargebee.com/docs/api/invoices?lang=java#list_invoices_for_a_customer.
* Retrieve transactions for a customer. See https://apidocs.chargebee.com/docs/api/transactions?lang=java#list_transactions_for_a_customer.

APIs updated:
* Now, a customer(without subscription) can be charged(Create invoice for Charge) for one time charges. See https://apidocs.chargebee.com/docs/api/invoices?lang=java#create_invoice_for_charge.
* Now, a customer(without subscription) can be charged for one time addons(Create invoice for Addon). See https://apidocs.chargebee.com/docs/api/invoices?lang=java#create_invoice_for_addon.

### v1.1.43 (2014-05-28)
* * *
New API to support Single Sign-on (SSO) to access the customer portal, if you already have your own authentication for your website. See https://apidocs.chargebee.com/docs/api/portal_sessions?lang=java.

### v1.1.42 (2014-05-23)
* * *
* New API to create customer without subscription. See https://apidocs.chargebee.com/docs/api/customers#create_a_customer

* New API to fetch invoices for a customer. This helps you fetch the invoices created due to multiple subscriptions present for any customer. See https://apidocs.chargebee.com/docs/api/invoices#list_invoices_for_a_customer

* PORTAL as event source added to indicate any changes initiated via Customer Portal. 

* Customer id reference is added to the invoice attributes.

### v1.1.41  (2014-04-30)
* * *
Adding missing fields that were not returned for address resource.

### v1.1.40  (2014-04-22)
* * *
Support for returning shipping address as part of create/update subscription API.

### v1.1.39  (2014-04-17)
* * *
Issue fix. For linked invoices and transactions, the enum values are used directly from Invoice & Transaction resource to represent type & status attributes.

### v1.1.38  (2014-03-25)
* * *
* Now the [Transaction attributes](https://apidocs.chargebee.com/docs/api/transactions#transaction_attributes "Transaction attributes") contains the details about the linked invoices.

* Now the [Invoice attributes](https://apidocs.chargebee.com/docs/api/invoices#invoice_attributes "Invoice attributes") contains the details about the linked transactions.

* Support for recording a payment received via offline mode. See our API documentation on [Record Payment for an Invoice](https://apidocs.chargebee.com/docs/api/transactions#record_payment_for_an_invoice "Record Payment for an Invoice")

### v1.1.37  (2014-03-19)
* * *
Support for deleting the plans & addons. See our API documentation on [Delete a plan](https://apidocs.chargebee.com/docs/api/plans#delete_a_plan "Delete a plan") & [Delete an addon](https://apidocs.chargebee.com/docs/api/addons#delete_an_addon "Delete an addon").

### v1.1.35  (2014-03-10)
* * *
* Support for creating coupons on the fly via API

* Support for updating the plans & addons.

* Now our hosted pages can be shown as popup checkout using our javascript API.

### v1.1.34  (2014-02-19)
* * *
* Support for passing shipping address for create subscription & update subscription API

* Added new attributes for the Address resource.

### v1.1.33  (2014-02-12)
* * *
* New resource Download added to expose the URLs from which you can download resources like invoice PDFs.

* Update card hosted page now support pass_thru_parameter like the checkout pages.

* Support for downloading invoice as PDF.

* Transaction resource now exposes the void description for transactions that are voided.

### v1.1.32  (2014-02-02)
* * *
Support for refund invoice and transaction.

### v1.1.31  (2014-01-26)
* * *
* Support for creating plans & addons on the fly via API.

* Support for handling double data type params handled. Eg., download_penality param for create new plan.

### v1.1.30  (2014-01-18)
* * *
Support addedBy attribute as input while creating comment. This can be used to pass information about who added the comment. If not provided, the value will be name of the api key.

### v1.1.29  (2014-01-16)
* * *
* Adding object that represent comments resource. Now comments can be added to the entities - Subscription, Invoice, Transaction, Plan, Addon & Coupon.

* API to fetch multiple subscriptions of a customer.

* Added support to get the list of events filtered by event type. Events can be fetched based on the event type eg., payment_succeeded.
