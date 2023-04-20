import pandas as pd
import numpy as np

# Define color palettes
custom_palette = ['#8c510a', '#d8b365', '#f6e8c3', '#c7eae5', '#5ab4ac', '#01665e', '#762a83', '#80cdc1', '#35978f', '#bf812d', '#dfc27d', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
setpoint_symbol_palette = ['o', 's', 'D', 'p', '^', '<', '>', '*', 'v', 'h']
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def TwoListToDict(categories,colorSelection):
    colorDict = {}
    for key in categories:
        for value in colorSelection:
            colorDict[key] = value
            colorSelection.remove(value)
            break
    return colorDict


def plotFlueGasStatter(ax,df, xKey,yKey,yErrKey,cDict1,cDict2):
    categoriesSetpoint = df['Setpoint SPJ temp'].unique()    
    setpoint_symbol_dict = dict(zip(categoriesSetpoint, setpoint_symbol_palette))
    salir =  False
    # ErrorBars
    #print('ErrorBars')
    if ( xKey not in df.columns.tolist() ):
        salir =  True
        print(bcolors.WARNING + xKey + "Is not a xKey in DataFrame"+ bcolors.ENDC)
    if ( yKey not in df.columns.tolist() ):
        salir =  True
        print( bcolors.WARNING + yKey + "Is not a yKey in DataFrame" + bcolors.ENDC)

    if salir:
        print(bcolors.FAIL + "No plotting for " + xKey + " with " + yKey + bcolors.ENDC)
        return ax


    ax.errorbar(df[xKey],
             df[yKey],
             yerr=df[yErrKey],
             fmt='',linestyle='',color='black')
    # Circles    
    cirkel_marker_style = dict(marker='o', linestyle='None', markersize=10,
                            fillstyle=None,  markerfacecolor='None',
                            markeredgewidth=2)
    grouped = df.groupby('Setpoint SPJ temp')
    for key, group in grouped:
        ax.plot(group[xKey], group[yKey],  
        #s = 200+0*group['Em_con_NOx_mgNO2_Nm-3'],
        label=key, marker=setpoint_symbol_dict[key], linestyle='', markerfacecolor='white', markeredgecolor=cDict2[key], markersize=8)    

    #Main Dots
    # 
    filled_marker_style = dict(marker='o', linestyle='None', markersize=6,
                            markeredgecolor='None')
    grouped = df.groupby('A_Feedstock_name')
    for key, group in grouped:
        ax.plot(group[xKey], group[yKey],
        label=key, markerfacecolor=cDict1[key],**filled_marker_style)          

    #ax.set_xlim([700,1000])
    #ax.set_ylim([0,600])
    ax.set_xlabel(xKey)
    ax.set_ylabel(yKey)
    ax.set_title(yKey)
    ax.grid()

    # Fixing Legend
    # Shrink current axis's height by 10% on the bottom
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.4,
                    box.width, box.height * 0.6])
    # Put a legend below current axis
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25),
            fancybox=True, shadow=True, ncol=3)
    return(ax)


 #   bar_colors = ['#8c510a','#8c510a','#8c510a',
  #            '#d8b365','#d8b365','#d8b365','#d8b365',
   #           '#f6e8c3','#f6e8c3','#f6e8c3',
    #          '#c7eae5','#c7eae5','#c7eae5','#c7eae5',
     #         '#5ab4ac','#5ab4ac','#5ab4ac','#5ab4ac',
      #        '#01665e',
       #       '#762a83',]
  #array, without outliers   
#'tab:green', orange, blue, red, purple, olive, cyan. Alternative colour scheme

def plotBarCharts(ax,columns, height,error,bar_labels, group = [], group_offset=1.0, user_width = 1.0):
    bar_colors = ['#8c510a','#8c510a','#8c510a','#8c510a',
              '#d8b365','#d8b365','#d8b365','#d8b365',
              '#f6e8c3','#f6e8c3','#f6e8c3',
              '#c7eae5','#c7eae5','#c7eae5','#c7eae5',
              '#5ab4ac','#5ab4ac','#5ab4ac','#5ab4ac',
              '#01665e','#01665e',
              '#762a83','#762a83',]

           
#    alfa_array  =  [0.6,0.8,1,
 #                   0.4,0.6,0.8,1,
  #                  0.4,0.6,1,
   #                 0.4,0.6,0.8,1,
    #                0.4,0.6,0.8,1,
     #               0.6,
      #              0.6]
    alfa_array  =  [0.4,0.6,0.8,1,
                    0.4,0.6,0.8,1,
                    0.4,0.6,1,
                    0.4,0.6,0.8,1,
                    0.4,0.6,0.8,1,
                    0.6,1,
                    0.6,1]
    offset_i = 0.0
    xi = 1.0*np.array(range(0,len(columns)))
    for i in range(0,len(columns)):
    #idx[i] = 2*i
        # For plotting offset between the groups
        if (len(group) > 0  and i>0):
            if group[i]!=group[i-1]:
                offset_i = group_offset
            else:
                offset_i = 0.0
        xi[i:len(xi)] = xi[i:len(xi)] +  offset_i
        if len(bar_labels) > 0: 
            ax.bar(xi[i],height[i] , label=bar_labels[i],width=user_width, color=bar_colors[i], alpha = alfa_array[i],align='edge')
        else:
            ax.bar(xi[i],height[i] ,width=user_width, color=bar_colors[i], alpha = alfa_array[i],align='edge')
        if len(error) > 0: ax.errorbar(xi[i]+user_width/2,height[i], yerr=100*error[i], fmt="", color="k")    
        if len(bar_labels) > 0:
            ax.set_xticks(xi)
            ax.set_xticklabels(bar_labels, rotation = 45,fontsize=8)

#when making matrix bars with %, multiply the error by 100: yerr=100*error[i]
    return(ax)
