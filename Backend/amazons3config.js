const AWS = require('aws-sdk');

//configuring the AWS environment
AWS.config.update({
    accessKeyId: "AKIAJES4NA2UXSQVD5VQ",
    secretAccessKey: "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"
  });

module.exports = AWS;
