/**
 * Created by john on 19/10/2017.
 */

  //redirect console log
(function () {
            if (!console) {
                console = {};
            }
            var old = console.log;
            var logger = document.getElementById('console');
            console.log = function (message) {
                if (typeof message == 'object') {
                    logger.innerHTML += (JSON && JSON.stringify ? JSON.stringify(message) : String(message)) + '<br />';
                } else {
                    logger.innerHTML += message + '<br />';
                }
            }
        })();