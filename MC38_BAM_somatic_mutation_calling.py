
import os

#Create index file and dict file for the reference data file 
os.chdir('/home/raymond/Desktop/mouse_genome_mm10') #change me
os.system('samtools faidx /home/raymond/Desktop/mouse_genome_mm10/mm10.fa') #change me
os.system('samtools dict /home/raymond/Desktop/mouse_genome_mm10/mm10.fa -o mm10.fa.dict') #change me


#Create index file for the MC38 mouse tumor bam file
os.chdir('/home/raymond/Desktop/sambamdata/MC38_chromosome')

for i in range(1, 20):
    file_bam  = 'MC38_chr{}.bam'.format(i)
    os.system("samtools index '/home/raymond/Desktop/sambamdata/MC38_chromosome/%s'" % (file_bam))

os.system("samtools index '/home/raymond/Desktop/sambamdata/MC38_chromosome/MC38_chrM.bam'")
os.system("samtools index '/home/raymond/Desktop/sambamdata/MC38_chromosome/MC38_chrX.bam'")
os.system("samtools index '/home/raymond/Desktop/sambamdata/MC38_chromosome/MC38_chrY.bam'")


#run somatic variant calling without normal sample matchedUse by using GATK4 Mutect2 
os.chdir('/home/raymond/Desktop/MC38_BAM_somatic_mutation_calling')

for i in range(1, 20):
    file_bam  = 'MC38_chr{}.bam'.format(i)
    file_vcf = 'MC38_chr{}.vcf'.format(i)
    os.system("gatk Mutect2 -R '/home/raymond/Desktop/mouse_genome_mm10/mm10.fa' -I '/home/raymond/Desktop/sambamdata/MC38_chromosome/%s' -O %s" %(file_bam, file_vcf))

os.system("gatk Mutect2 -R '/home/raymond/Desktop/mouse_genome_mm10/mm10.fa' -I '/home/raymond/Desktop/sambamdata/MC38_chromosome/MC38_chrM.bam' -O MC38_chrX.vcf")
os.system("gatk Mutect2 -R '/home/raymond/Desktop/mouse_genome_mm10/mm10.fa' -I '/home/raymond/Desktop/sambamdata/MC38_chromosome/MC38_chrX.bam' -O MC38_chrY.vcf")
os.system("gatk Mutect2 -R '/home/raymond/Desktop/mouse_genome_mm10/mm10.fa' -I '/home/raymond/Desktop/sambamdata/MC38_chromosome/MC38_chrY.bam' -O MC38_chrY.vcf")
