source("https://bioconductor.org/biocLite.R")
biocLite("karyoploteR")
library(karyoploteR)

#load ERV dataset
data2 <-read.csv("/Users/vithusaaselva1/Desktop/ERV.csv")
head(data2)

#chromosome row number
chromo2 <- data2[data2$genoName == "chr", ]
chromo2

#genoName
Gname2<-(data2[1] == "chr1")
Gname2

#genoStart
gstart2 <- data2$genoStart

#genoEND
gend2 <- data2$genoEnd

#funtion for genoStart

function3 <- function(chr){
  Gname2<-(data2[1] == chr)
  gstart2 <- data2$genoStart[Gname2]
  return(gstart2)
}

#function for genoEnd

function4 <- function(chr){
  Gname2<-(data2[1] == chr)
  gend2 <- data2$genoEnd[Gname2]
  return(gend2)
}

#call function for each chromosome start and end

chr1st <- function3("chr1")
chr1en <- function4("chr1")

chr2st <- function3("chr2")
chr2en <- function4("chr2")

chr3st <- function3("chr3")
chr3en <- function4("chr3")

chr4st <- function3("chr4")
chr4en <- function4("chr4")

chr5st <- function3("chr5")
chr5en <- function4("chr5")

chr6st <- function3("chr6")
chr6en <- function4("chr6")

chr7st <- function3("chr7")
chr7en <- function4("chr7")

chr8st <- function3("chr8")
chr8en <- function4("chr8")

chr9st <- function3("chr9")
chr9en <- function4("chr9")

chr10st <- function3("chr10")
chr10en <- function4("chr10")

chr11st <- function3("chr11")
chr11en <- function4("chr11")

chr12st <- function3("chr12")
chr12en <- function4("chr12")

chr13st <- function3("chr13")
chr13en <- function4("chr13")

chr14st <- function3("chr14")
chr14en <- function4("chr14")

chr15st <- function3("chr15")
chr15en <- function4("chr15")

chr16st <- function3("chr16")
chr16en <- function4("chr16")

chr17st <- function3("chr17")
chr17en <- function4("chr17")

chr18st <- function3("chr18")
chr18en <- function4("chr18")

chr19st <- function3("chr19")
chr19en <- function4("chr19")

chr20st <- function3("chr20")
chr20en <- function4("chr20")

chr21st <- function3("chr21")
chr21en <- function4("chr21")

chr22st <- function3("chr22")
chr22en <- function4("chr22")

chrXst <- function3("chrX")
chrXen <- function4("chrX")

chrYst <- function3("chrY")
chrYen <- function4("chrY")


# store chromosome start and end info in GRanges object

chr1d <- toGRanges(
  data.frame(
    chr=c("chr1"), start= c(chr1st),end= c(chr1en)))

chr2d <- toGRanges(
  data.frame(
    chr=c("chr2"), start= c(chr2st),end= c(chr2en)))

chr3d <- toGRanges(
  data.frame(
    chr=c("chr3"), start= c(chr3st),end= c(chr3en)))

chr4d <- toGRanges(
  data.frame(
    chr=c("chr4"), start= c(chr4st),end= c(chr4en)))

chr5d <- toGRanges(
  data.frame(
    chr=c("chr5"), start= c(chr5st),end= c(chr5en)))

chr6d <- toGRanges(
  data.frame(
    chr=c("chr6"), start= c(chr6st),end= c(chr6en)))

chr7d <- toGRanges(
  data.frame(
    chr=c("chr7"), start= c(chr7st),end= c(chr7en)))

chr8d <- toGRanges(
  data.frame(
    chr=c("chr8"), start= c(chr8st),end= c(chr8en)))

chr9d <- toGRanges(
  data.frame(
    chr=c("chr9"), start= c(chr9st),end= c(chr9en)))

chr10d <- toGRanges(
  data.frame(
    chr=c("chr10"), start= c(chr10st),end= c(chr10en)))

chr11d <- toGRanges(
  data.frame(
    chr=c("chr11"), start= c(chr11st),end= c(chr11en)))

chr12d <- toGRanges(
  data.frame(
    chr=c("chr12"), start= c(chr12st),end= c(chr12en)))

chr13d <- toGRanges(
  data.frame(
    chr=c("chr13"), start= c(chr13st),end= c(chr13en)))

chr14d <- toGRanges(
  data.frame(
    chr=c("chr14"), start= c(chr14st),end= c(chr14en)))

chr15d <- toGRanges(
  data.frame(
    chr=c("chr15"), start= c(chr15st),end= c(chr15en)))

chr16d <- toGRanges(
  data.frame(
    chr=c("chr16"), start= c(chr16st),end= c(chr16en)))

chr17d <- toGRanges(
  data.frame(
    chr=c("chr17"), start= c(chr17st),end= c(chr17en)))

chr18d <- toGRanges(
  data.frame(
    chr=c("chr18"), start= c(chr18st),end= c(chr18en)))

chr19d <- toGRanges(
  data.frame(
    chr=c("chr19"), start= c(chr19st),end= c(chr19en)))

chr20d <- toGRanges(
  data.frame(
    chr=c("chr20"), start= c(chr20st),end= c(chr20en)))

chr21d <- toGRanges(
  data.frame(
    chr=c("chr21"), start= c(chr21st),end= c(chr21en)))

chr22d <- toGRanges(
  data.frame(
    chr=c("chr22"), start= c(chr22st),end= c(chr22en)))

chrXd <- toGRanges(
  data.frame(
    chr=c("chrX"), start= c(chrXst),end= c(chrXen)))

chrYd <- toGRanges(
  data.frame(
    chr=c("chrY"), start= c(chrYst),end= c(chrYen)))


#plot karyoplot

kp <- plotKaryotype(genome="hg38", plot.type=1, main="ERV chromosome start and end ranges", cex=0.6)

kpAddBaseNumbers(kp)

kpPlotRegions(kp, data= chr1d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr2d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr3d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr4d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr5d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr6d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr7d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr8d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr9d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr10d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr11d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr12d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr13d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr14d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr15d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr16d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr17d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr18d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr19d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr20d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr21d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chr22d, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chrXd, col="#7DDBD9", r0=0, r1=0.5)

kpPlotRegions(kp, data= chrYd, col="#7DDBD9", r0=0, r1=0.5)

 
