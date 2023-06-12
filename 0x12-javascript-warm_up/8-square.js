#!/usr/bin/node
!isNaN(process.argv[2])
  ? ((myVal) => {
      for (let i = 0; i < myVal; i++) {
        console.log('X'.repeat(myVal));
      }
    })(parseInt(process.argv[2]))
  : console.log('Missing size');
