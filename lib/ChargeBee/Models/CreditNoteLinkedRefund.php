<?php

class ChargeBee_CreditNoteLinkedRefund extends ChargeBee_Model
{
  protected $allowed = array('txn_id', 'applied_amount', 'applied_at', 'txn_status', 'txn_date', 'txn_amount', 'refund_reason_code');

}

?>