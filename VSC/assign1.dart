void main()
{
  var day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
  var hazeLevel = [125, 131, 121, 108, 96, 100, 120];
  var min = 9999;
  var max = 0;
  String minDay;
  String maxDay;
  
  print('Average PM2.5 readings for the week is $hazeLevel');

  for(var i = 0; i < hazeLevel.length; i++)
  {
    if(min > hazeLevel[i])
    {
      min = hazeLevel[i];
      minDay = day[i];
    }
  }
  print('Minimum reading for the week is $min on $minDay');

  for (var i = 0; i < hazeLevel.length; i++) 
  {
    if(max < hazeLevel[i])
    {
      max = hazeLevel[i];
      maxDay = day[i];
    }
  }
  print('Maximum reading for the week is $max on $maxDay');

}