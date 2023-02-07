the data in this folder is structured with minimal change with the original,
the difference is the way to determine the age range, instead of having a range
I took only the higher value of the range to simplify the programming expirience,
per example, the original csv was:

  0-4, 1362494, 1300996

processed:

  4, 1362494, 1300996

in the case of the last line that can be seen the age to be "100+" that case
will be an exception, instead of treating it like a "maximun", I would treat it
like a "minimun".

Also another change was made, instead of having the male and female in two separated
columns I decided to put it in the same column and add a colum that determines the genderanother differences in the genders, is that male data is in negative numbers to facilitate the plotting of the data, if you want there's a snippet I made that that would change the data back to positive.

If you want to transform more data you can add a folder in the preprocessed folder,
and under the utils folder there's a python file that process the data and adds it to
the "processed" folder.
