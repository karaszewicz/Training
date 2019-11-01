// Node RED function node to generate random points to be used in linear regression model training.
// Author: V.Kaznovsky
var slope_a = context.get('slope_a') || 1.5; 
var intercept = context.get('intercept') || 0.5;
var epsilon = context.get('epsilon') || 10;
var x=0, y=0;
var xypoints = context.get('xypoints') || 'x,y';
var mesg={};
mesg.payload='';

switch (msg.payload) {
    case 0 :
        {
            mesg.payload=xypoints;
            return[mesg];
        }
    case 1 :
        {   for (i = 0; i < 30; i++) 
            {
            epsilon= Math.floor((Math.random() * 10) + 1);
            x = Math.floor((Math.random() * 100) + 1);
            y = slope_a*x+intercept+epsilon/100;
            xypoints=xypoints+"\n"+x.toString()+','+y.toString();
            context.set('xypoints',xypoints);
            }
        }
        break;
    default:

        break;
}
