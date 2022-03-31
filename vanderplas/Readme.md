# My study notes on VanderPlas book
Post my own work here.  Reproduced examples and my applications/extensions.  

Reference: 
Python Data Science Handbook (essential tools), by Jake VanderPlas, c 2017.   
 * Amazon link:  
 * Github Repo:  https://github.com/jakevdp/PythonDataScienceHandbook

<img src="./PDSH-cover.png" width="180" height="auto" />

### To Focus on **VanderPlas book exclusively** for reproduced projects.  

  * Numpy this week and last week, 9/3/2019.  
  * Worked on Section 2.01 - 2.05 today.  

  * Matplotlib chapter finished. 
    - Blog write - Object Oriented vs Pyplot methods, 3D Surface, Geomapping.

  * Pandas chapter review cell selection commands - June 30, 2021. 
    - (iloc for index numbers, loc for named labels, at for single cell)
    - when multiple columns, row selected by label, it becomes a list, 2nd bracket
      df.loc[0:5, ['colA', 'colB', 'colC']] = "values"
      df.loc[0, 'colA'] = "one-value'  (here "0" without quotes is a label name)
      df.iloc[3, 1] = "new-value"  (select row-4, col-2 by index ref)
      df[label0(3:6), :] = "selected rows"  (label0 is named range for col 0)
      dictionary method to assign values to row-col.  
      boolean filters  

 * Scikit-Learn - July 2021 to finish  
   - Face Recognition, histogram of gradients, woman astronaut image