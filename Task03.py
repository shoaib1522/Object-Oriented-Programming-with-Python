def degree_locator(file_name):
    file=open(file_name,'r')
    readlines=file.read()
    count_of_lines=0
    file.seek(0)
    file.readline()
    file.readline()
    for i in range(len(readlines)):
        if readlines[i]=='\n':
            count_of_lines+=1
    file.seek(0)
    file.readline()
    file.readline()
    list_SE=[]
    list_IT=[]
    for j in range((count_of_lines)-2):
        line=file.readline()
        try:
            var=line.split('BSE')
            if var[0]=='':
                list_SE.append(line)
        except:
            continue
        try:
            var=line.split('BIT')
            if var[0]=='':
                list_IT.append(line)
        except:
            continue
    return list_SE,list_IT
def splitting_data(list):
    roll_no=[]
    first_namel=[]
    second_namel=[]
    DLD=[]
    ITC=[]
    PF=[]
    for i in range(len(list)):
        text=''+list[i]
        roll=text[0:10]
        if i==0:
            roll_no.append(roll)
        if roll not in roll_no:
            roll_no.append(roll)
    for loop in range(len(list)):
        line=''+list[loop]
        data=line[10:]
        first_name,second_name,crs,md,ss,fn=data.split(maxsplit=5)
        if loop==0:
            first_namel.append(first_name)
            second_namel.append(second_name)
        if first_name not in first_namel:
            first_namel.append(first_name)
        if second_name not in second_namel:
            second_namel.append(second_name)
        total=int(md)+int(ss)+int(fn)
        if crs=='DLD':
            DLD.append(total)
        elif crs=='ITC':
            ITC.append(total)
        elif crs=='PF':
            PF.append(total)
    return roll_no ,first_namel,second_namel,ITC,PF,DLD
def total_of_roll(ITC,PF,DLD):
    total=[]
    for calculation in range(len(ITC)):
        measure=ITC[calculation]+PF[calculation]+DLD[calculation]
        total.append(measure)
    return total 
def percentages(total):
    percentage=[]
    for percent in range(len(total)):
        value=round(total[percent]*100/300,1)
        percentage.append(value)
    return percentage
def grades(percentage):
    grade_list=[]
    for grade in range(len(percentage)):
        if percentage[grade]>=85:
            grade_list.append('A')
        elif percentage[grade]>=80 and  percentage[grade]<85:
            grade_list.append('A-')
        elif percentage[grade]>=75 and percentage[grade]<80:
            grade_list.append('B+')
        elif percentage[grade]>=70 and percentage[grade]<75:
            grade_list.append('B')
        elif percentage[grade]>=65 and percentage[grade]<70:
            grade_list.append('B-')
        elif percentage[grade]>=61 and percentage[grade]<65:
            grade_list.append('C+')
        elif percentage[grade]>=58 and percentage[grade]<=60:
            grade_list.append('C')
        elif percentage[grade]>=55 and percentage[grade]<=57:
            grade_list.append('C-')
        elif percentage[grade]>=50 and percentage[grade]<55:
            grade_list.append('D')
        elif percentage[grade]<50:
            grade_list.append('F')
    return grade_list
def department_averages(list):
    average=0
    for i in range(len(list)):
        average+=list[i]
    average=round(average/len(list),0)     
    return int(average)      
def make_lengths_equal(list1,list2):
    if len(list1)>len(list2):
        for i in range(len(list1)-len(list2)):
            list2.append(0)
    if len(list1)<len(list2):
        for i in range(len(list2)-len(list1)):
            list1.append(0)
    return list1,list2
def overall_averages(list1,list2):
    mean=0
    for i in range(len(list1)):
        mean+=list1[i]+list2[i]
    mean=mean/(len(list1)+len(list2))
    return int(mean)
def main():
    degree_se,degree_it=degree_locator('grades_updated.txt')
    Roll_Numbers_se,first_names_se,second_names_se,itc_se,pf_se,dld_se=splitting_data(degree_se)
    Roll_Numbers_it,first_names_it,second_names_it,itc_it,pf_it,dld_it=splitting_data(degree_it)
    totals_se=total_of_roll(itc_se,pf_se,dld_se)
    totals_it=total_of_roll(itc_it,pf_it,dld_it)
    percentages_se=percentages(totals_se)
    percentages_it=percentages(totals_it)
    grade_se=grades(percentages_se)
    grade_it=grades(percentages_it)
    itc_se_average=department_averages(itc_se)
    pf_se_average=department_averages(pf_se)
    dld_se_average=department_averages(dld_se)
    itc_it_average=department_averages(itc_it)
    pf_it_average=department_averages(itc_it)
    dld_it_average=department_averages(itc_it)
    totals_se_average=department_averages(totals_se)
    totals_it_average=department_averages(totals_it)
    itc_se_upd,itc_it_upd=make_lengths_equal(itc_se,itc_it)
    pf_se_upd,pf_it_upd=make_lengths_equal(pf_se,pf_it)
    dld_se_upd,dld_it_upd=make_lengths_equal(dld_se,dld_it)
    totals_se_upd,totals_it_upd=make_lengths_equal(totals_se,totals_it)
    overall_mean_itc=overall_averages(itc_se_upd,itc_it_upd)
    overall_mean_pf=overall_averages(pf_se_upd,pf_it_upd)
    overall_mean_dld=overall_averages(dld_se_upd,dld_it_upd)
    overall_mean_totals=overall_averages(totals_se_upd,totals_it_upd)
    print(' '*18+'University Of the Punjab\n'+' '*14+'College of Information Technology\n'+' '*16+'Result Session : Spring 2010')
    print('Degree: BIT')
    print('Sr.No.'+' '+'Roll No.'+' '*3+'Student Name'+' '*19+'ITC'+' '*2+'PF'+' '+'DLD'+' '+'Total'+' '+'%'+'age'+' '+'Grade')
    print('='*6+' '+'='*10+' '+'='*30+' '+'='*3+' '+'='*3+' '+'='*3+' '+'='*5+' '+'='*4+' '+'='*5)
    for i in range(len(Roll_Numbers_it)):
        print(' '*4+f'{i+1}'+' '*2+f'{Roll_Numbers_it[i]}'+' '+f'{first_names_it[i]} {second_names_it[i]}'+' '*(30-len(first_names_it[i])-len(second_names_it[i]))+' '+f'{itc_it[i]}'+' '*2+f'{pf_it[i]}'+' '*2+f'{dld_it[i]}'+' '*3+f'{totals_it[i]}'+' '+f'{percentages_it[i]}'+' '*3+f'{grade_it[i]}')
    print(' '*49+'='*28)
    print(' '*29+'BIT Degree Average:'+' '*2+f'{itc_it_average}  {pf_it_average}  {dld_it_average}   {totals_it_average}')
    print('Degree: BSE')
    print('Sr.No.'+' '+'Roll No.'+' '*3+'Student Name'+' '*19+'ITC'+' '*2+'PF'+' '+'DLD'+' '+'Total'+' '+'%'+'age'+' '+'Grade')
    print('='*6+' '+'='*10+' '+'='*30+' '+'='*3+' '+'='*3+' '+'='*3+' '+'='*5+' '+'='*4+' '+'='*5)
    for i in range(len(Roll_Numbers_se)):
        print(' '*4+f'{i+1}'+' '*2+f'{Roll_Numbers_se[i]}'+' '+f'{first_names_se[i]} {second_names_se[i]}'+' '*(30-len(first_names_se[i])-len(second_names_se[i]))+' '+f'{itc_se[i]}'+' '*2+f'{pf_se[i]}'+' '*2+f'{dld_se[i]}'+' '*3+f'{totals_se[i]}'+' '+f'{percentages_se[i]}'+' '*3+f'{grade_se[i]}')
    print(' '*49+'='*28)
    print(' '*29+'BSE Degree Average:'+' '*2+f'{itc_se_average}  {pf_se_average}  {dld_se_average}   {totals_se_average}')
    print(' '*49+'='*28)
    print(' '*32+'Over All Average:'+' '*1+f'{overall_mean_itc}  {overall_mean_pf}  {overall_mean_dld}   {overall_mean_totals}')
main()

    