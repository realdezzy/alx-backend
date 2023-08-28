#!/usr/bin/node
/**
 * Queing system
 */

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error("Jobs is not an array")
    }
    for (let element of jobs) {

        let job = queue.create('push_notification_code_3', element)
    
        job.on('complete', function() {
            console.log(`Notification job ${job.id} completed`);
        })
    
        job.on('progress', function(progress, data) {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        })
    
        job.on('failed', function(error) {
            console.log(`Notification job ${job.id} failed: ${error.message || error.toString()}`);
        });

        job.save( function(err){
            if( !err ) console.log( `Notification job created: ${job.id}` );
        });
    
    };
}


module.exports = createPushNotificationsJobs;
