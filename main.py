#!/home/miniconda3/bin/python

'''
Pipeline for the analysis of CamelPox virus
the fastq files in .gz formate should be in home directory 
for any query write at suheelhamdani@gmail.com



'''

from ctypes import alignment
import sys
import os
import subprocess

from Bio.Sequencing.Applications import BwaMemCommandline


'''


task1=subprocess.Popen(['prefetch','max-size 30g',user_input])
task1.wait()
with open("validate.txt","wb") as f:
    task2=subprocess.Popen(['vdb-validate',user_input],stdout=f)
f.close()
task2.wait()

task3=subprocess.Popen(['fasterq-dump',user_input])
task3.wait()



     
#assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
#f = open(user_input,'r+')
task4 = subprocess.Popen(['fastqc',user_input+'_1.fastq',user_input+'_2.fastq'])
task4.wait()'''

ref='/home/shared/CamPox-Virus/Reff-Index/96Campoxrefrence.fa'

#list=['V350023222_L04_1_','V350023222_L04_2_']

#list=['V350023222_L04_1_','V350023222_L04_2_','V350023222_L04_3_','V350023222_L04_4_','V350023222_L04_5_','V350023222_L04_6_','V350023222_L04_18_','V350023222_L04_7_','V350023222_L04_8_','V350023222_L04_17_','V350023222_L04_19_','V350023222_L04_20_','V350023222_L04_21_','V350023222_L04_22_','V350023222_L04_23_','V350023222_L04_24_','V350023222_L04_25_']
list=['V350023222_L04_7_','V350023222_L04_8_','V350023222_L04_17_','V350023222_L04_18_']

#list=['V350023222_L04_1_']

taskdel=subprocess.Popen(['rm','-rf','output'])
taskdel.wait()

task_01=subprocess.Popen(['mkdir','output'])
task_01.wait()

n=1

for sample in list:
    task_02=subprocess.Popen(['mkdir','output'+'/'+sample])
    task_02.wait()







for seq in list:
    task_mkdir_fastqc_before=subprocess.Popen(['mkdir','output'+'/'+seq+'/'+'fastqc_before'])
    task_mkdir_fastqc_before.wait()


    task_fastqc_1 = subprocess.Popen(['fastqc','-t','12','-o','output'+'/'+seq+'/'+'fastqc_before' ,'Camel'+str(n)+'/'+seq+'1.fq.gz','Camel'+str(n)+'/'+seq+'2.fq.gz'])
    task_fastqc_1.wait()
    
    task_mkdir_trim=subprocess.Popen(['mkdir','output'+'/'+seq+'/'+'trim'])
    task_mkdir_trim.wait()

    task_trim=subprocess.Popen(['trimmomatic', 'PE','-threads','12','Camel'+str(n)+'/'+seq+'1.fq.gz','Camel'+str(n)+'/'+seq+'2.fq.gz','output'+'/'+seq+'/'+'trim'+'/'+seq+'.trimmed_1.fq','output'+'/'+seq+'/'+'trim'+'/'+seq+'_un.trimmed_1.fq','output'+'/'+seq+'/'+'trim'+'/'+seq+'.trimmed_2.fq','output'+'/'+seq+'/'+'trim'+'/'+seq+'_un.trimmed_2.fq','SLIDINGWINDOW:4:20'])
    task_trim.wait()


    #task_mkdir_assembly=subprocess.Popen(['mkdir','output'+'/'+seq+'/'+'assembly'])
    #task_mkdir_assembly.wait()

    #task_assembly=subprocess.Popen(['spades.py','-t','32','-1','output'+'/'+seq+'/'+'trim'+'/'+seq+'.trimmed_1.fq','-2','output'+'/'+seq+'/'+'trim'+'/'+seq+'.trimmed_2.fq','--trusted-contigs',ref,'-t','10','--careful','-o','output'+'/'+seq+'/'+'assembly'])
    #task_assembly.wait()

    task_mkdir_fastqc_after_trim=subprocess.Popen(['mkdir','output'+'/'+seq+'/'+'fastqc_after_trim'])
    task_mkdir_fastqc_after_trim.wait()

    task_fastqc_2 = subprocess.Popen(['fastqc','-t','12','-o','output'+'/'+seq+'/'+'fastqc_after_trim' ,'output'+'/'+seq+'/'+'trim'+'/'+seq+'.trimmed_1.fq','output'+'/'+seq+'/'+'trim'+'/'+seq+'.trimmed_2.fq'])
    task_fastqc_2.wait()
    
    n=n+1
     
    task_mkdir_alignment=subprocess.Popen(['mkdir','output'+'/'+seq+'/'+'alignment_sam'])
    task_mkdir_alignment.wait()

    
    #read_file1p='output'+'/'+seq+'/'+'trim'+'/'+seq+'.trimmed_1.fq'
    #read_file2p='output'+'/'+seq+'/'+'trim'+'/'+seq+'.trimmed_2.fq'
    #align_cmd = BwaMemCommandline(reference=ref, read_file1=read_file1p,read_file2=read_file2p,t=36)

    #with open('out-file.sam', 'w') as f:

    #with open('output'+'/'+seq+'/'+'alignment_sam'+'/'+seq+'.bwa.sam', 'w') as output:
    task_alignment=subprocess.Popen(['bwa','mem','-t','12',ref,'output'+'/'+seq+'/'+'trim'+'/'+seq+'.trimmed_1.fq','output'+'/'+seq+'/'+'trim'+'/'+seq+'.trimmed_2.fq','-o','output'+'/'+seq+'/'+'alignment_sam'+'/'+seq+'.bwa.sam'])
    task_alignment.wait()


    

    task_makedir_alignment_bam=subprocess.Popen(['mkdir','output'+'/'+seq+'/'+'alignment_bam'])
    task_makedir_alignment_bam.wait()

    task_sam_bam= subprocess.Popen(['samtools','view','-@','12','-b','output'+'/'+seq+'/'+'alignment_sam'+'/'+seq+'.bwa.sam','-o','output'+'/'+seq+'/'+'alignment_bam'+'/'+seq+'.bwa.bam'])
    task_sam_bam.wait()
    

    task_makedir_alignment_sorted_bam=subprocess.Popen(['mkdir','output'+'/'+seq+'/'+'alignment_sort_bam'])
    task_makedir_alignment_sorted_bam.wait()

    task_bam_sorted_bam=subprocess.Popen(['samtools','sort','-@','12','output'+'/'+seq+'/'+'alignment_bam'+'/'+seq+'.bwa.bam','-o','output'+'/'+seq+'/'+'alignment_sort_bam'+'/'+seq+'.bwa.sorted.bam'])
    task_bam_sorted_bam.wait()

    
    task_makedir_vcfs=subprocess.Popen(['mkdir','output'+'/'+seq+'/'+'vcfs'])
    task_makedir_vcfs.wait()

    task_makedir_vcfs=subprocess.Popen(['mkdir','output'+'/'+seq+'/'+'bcfs'])
    task_makedir_vcfs.wait()


    taskpipe1=subprocess.Popen(['bcftools','mpileup','--threads','12','-Ou','-d','100000','-f',ref,'output'+'/'+seq+'/'+'alignment_sort_bam'+'/'+seq+'.bwa.sorted.bam','-o','output'+'/'+seq+'/'+'bcfs'+'/'+seq+'.bcf'])
    taskpipe1.wait()

    taskpipe2=subprocess.Popen(['bcftools','call','-m','-v','-Oz','output'+'/'+seq+'/'+'bcfs'+'/'+seq+'.bcf','-o','output'+'/'+seq+'/'+'vcfs'+'/'+seq+'.vcf.gz'])
    taskpipe2.wait()
    
    



    #task_variant_call=subprocess.Popen(['bcftools','mpileup','--threads','12','-Ou','-d','100000','-f',ref,'output'+'/'+seq+'/'+'alignment_sort_bam'+'/'+seq+'.bwa.sorted.bam','|','bcftools','call','-mv','Oz','-o','output'+'/'+seq+'/'+'vcfs'+'/'+seq+'.vcf.gz'])
    #task_variant_call.wait()

    

    task_makedir_norm_bcf=subprocess.Popen(['mkdir','output'+'/'+seq+'/'+'norm_bcf'])
    task_makedir_norm_bcf.wait()

    task_norm_bcf=subprocess.Popen(['bcftools','norm','--threads','12','-f',ref,'output'+'/'+seq+'/'+'vcfs'+'/'+seq+'.vcf.gz','-o','output'+'/'+seq+'/'+'norm_bcf'+'/'+seq+'.norm.bcf'])
    task_norm_bcf.wait()
     
    

    task_makedir_norm_flt_indels_bcf=subprocess.Popen(['mkdir','output'+'/'+seq+'/'+'norm_flt_indels_bcf'])
    task_makedir_norm_flt_indels_bcf.wait()

    task_indels_bcf=subprocess.Popen(['bcftools','filter','--threads','12','-G','5','output'+'/'+seq+'/'+'norm_bcf'+'/'+seq+'.norm.bcf','-Ob','-o','output'+'/'+seq+'/'+'norm_flt_indels_bcf'+'/'+seq+'.norm.flt-indels.bcf'])
    task_indels_bcf.wait()

    

     
    task_makedir_index=subprocess.Popen(['mkdir','output'+'/'+seq+'/'+'index_indels'])
    task_makedir_index.wait()

    task_index=subprocess.Popen(['bcftools','index','--threads','12','output'+'/'+seq+'/'+'norm_flt_indels_bcf'+'/'+seq+'.norm.flt-indels.bcf'])
    task_index.wait()

    task_makedir_consensus=subprocess.Popen(['mkdir','output'+'/'+seq+'/'+'consensus'])
    task_makedir_consensus.wait()

    task_consensus=subprocess.Popen(['bcftools','consensus','-f',ref,'output'+'/'+seq+'/'+'norm_flt_indels_bcf'+'/'+seq+'.norm.flt-indels.bcf','-o','output'+'/'+seq+'/'+'consensus'+'/'+seq+'_consensus.fa'])
    task_consensus.wait()

    








    #task_mkdir_quast=subprocess.Popen(['mkdir','output'+'/'+seq+'/'+'quast'])
    #task_mkdir_quast.wait()

    #task_quast=subprocess.Popen(['quast','-r','96Campoxrefrence.fa','output'+'/'+seq+'/'+'assembly','-o','output'+'/'+seq+'/'+'quast'])
    #task_quast.wait()

    '''
     # docker run -it -v "$(pwd)"\SRR1693821:/input -v "$(pwd)"\SRR1693821:/output longqc sampleqc -x pb-sequel -p 10 -o /output/report /input/SRR1693821_1.fastq   '''





'''
    task_mkdir_assembly=subprocess.Popen(['mkdir','output'+'/'+seq+'/'+'assembly'])
    task_mkdir_assembly.wait()

    task_assembly=subprocess.Popen(['spades.py','-1','output'+'/'+seq+'/'+'trim'+'/'+seq+'trimmed_1.fq','-2','output'+'/'+seq+'/'+'trim'+'/'+seq+'trimmed_2.fq','--trusted-contigs',ref,'-t','10','--careful','-o','output'+'/'+seq+'/'+'assembly'])
    task_assembly.wait()
    '''
