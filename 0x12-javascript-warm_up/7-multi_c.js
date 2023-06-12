#!/usr/bin/node
!isNaN(process.argv[2])
  ? (() => {
      for (let i = 0; i < parseInt(process.argv[2]); i++) {
        console.log('C is fun');
      }
    })()
  : console.log('Missing number of occurrences');
