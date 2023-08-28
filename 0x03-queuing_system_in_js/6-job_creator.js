#!/usr/bin/node
/**
 * Queing system
 */

import { createQueue} from "kue";

const queue = createQueue()

const jobObj = { phoneNumber: '+2349022065161', message: 'Kindly verify your identification' };


const job = queue.create('push_notification_code', jobObj).save( function(err){
   if( !err ) console.log( `Notification job created: ${job.id}` );
});

job.on('complete', function(){
  console.log('Notification job completed');

})

job.on('failed', function(errorMessage){
  console.log('Notification job failed');});
