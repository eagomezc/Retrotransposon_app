# kpPlotDensity

#load LINE dataset

data1 <-read.csv("/Users/vithusaaselva1/Desktop/Line1.csv")
head(data1)

#chromosome column number

chromo <- data1[data1$genoName == "chr", ]

#genoName

Gname<-(data1[1] == "chr1")

#genoStart

gstart <- data1$genoStart

#genoEnd

gend <- data1$genoEnd


#************
# FUNCTIONS
#************

# @details

# call function and store information for each chromosome 
# start and end coordinates

# genoStart

function1 <- function(chr){
  Gname<-(data1[1] == chr)
  gstart <- data1$genoStart[Gname]
  return(gstart)
}

# genoEnd

function2 <- function(chr){
  Gname<-(data1[1] == chr)
  gend <- data1$genoEnd[Gname]
  return(gend)
}

#call function for each chromosome start and end

chr1start <- function1("chr1")
chr1end <- function2("chr1")

chr2start <- function1("chr2")
chr2end <- function2("chr2")

chr3start <- function1("chr3")
chr3end <- function2("chr3")

chr4start <- function1("chr4")
chr4end <- function2("chr4")

chr5start <- function1("chr5")
chr5end <- function2("chr5")

chr6start <- function1("chr6")
chr6end <- function2("chr6")

chr7start <- function1("chr7")
chr7end <- function2("chr7")

chr8start <- function1("chr8")
chr8end <- function2("chr8")

chr9start <- function1("chr9")
chr9end <- function2("chr9")

chr10start <- function1("chr10")
chr10end <- function2("chr10")

chr11start <- function1("chr11")
chr11end <- function2("chr11")

chr12start <- function1("chr12")
chr12end <- function2("chr12")

chr13start <- function1("chr13")
chr13end <- function2("chr13")

chr14start <- function1("chr14")
chr14end <- function2("chr14")

chr15start <- function1("chr15")
chr15end <- function2("chr15")

chr16start <- function1("chr16")
chr16end <- function2("chr16")

chr17start <- function1("chr17")
chr17end <- function2("chr17")

chr18start <- function1("chr18")
chr18end <- function2("chr18")

chr19start <- function1("chr19")
chr19end <- function2("chr19")

chr20start <- function1("chr20")
chr20end <- function2("chr20")

chr21start <- function1("chr21")
chr21end <- function2("chr21")

chr22start <- function1("chr22")
chr22end <- function2("chr22")

chrXstart <- function1("chrX")
chrXend <- function2("chrX")

chrYstart <- function1("chrY")
chrYend <- function2("chrY")

source("https://bioconductor.org/biocLite.R")
biocLite("karyoploteR")
library(karyoploteR)

# store chromosome start and end functions in GRanges object

#***************
#KpPlotDensity 
#***************


# @details


# \code{kpPlotDensity} Density of features (coordinates) are plotted along the genome represented by
# \code {GRanges} object through the length of the genome. It computes the number of features per chromosome 
# and ensures no overlapping flooring along the genome.
# \code {chr=c(x), start= c(y),end= c(z)}, firstly need to specify chromosome,
# the start coordinate, and then end coordinate
# Returns the regions where the chromosome coordinates should be located on the genome.


# @parameters 


# \code{kp} the initial argument for the data plotting functions of karyoplotR. Returned
# by calling \code{plotKaryotype}
# \code {data= chr1data} this is a GRanges object, from which density is computed
# \code {col= "#DBBDED"} specifies colour of the density plotted, in this case purple
# \code {r= r0=0, r1=0.5} specifies vertical range of data panel to sketch the plot


chr1data <- toGRanges(
  data.frame(
    chr=c("chr1"), start= c(chr1start),end= c(chr1end)))

chr2data <- toGRanges(
  data.frame(
    chr=c("chr2"), start= c(chr2start),end= c(chr2end)))

chr3data <- toGRanges(
  data.frame(
    chr=c("chr3"), start= c(chr3start),end= c(chr3end)))

chr4data <- toGRanges(
  data.frame(
    chr=c("chr4"), start= c(chr4start),end= c(chr4end)))

chr5data <- toGRanges(
  data.frame(
    chr=c("chr5"), start= c(chr5start),end= c(chr5end)))

chr6data <- toGRanges(
  data.frame(
    chr=c("chr6"), start= c(chr6start),end= c(chr6end)))

chr7data <- toGRanges(
  data.frame(
    chr=c("chr7"), start= c(chr7start),end= c(chr7end)))

chr8data <- toGRanges(
  data.frame(
    chr=c("chr8"), start= c(chr8start),end= c(chr8end)))

chr9data <- toGRanges(
  data.frame(
    chr=c("chr9"), start= c(chr9start),end= c(chr9end)))

chr10data <- toGRanges(
  data.frame(
    chr=c("chr10"), start= c(chr10start),end= c(chr10end)))

chr11data <- toGRanges(
  data.frame(
    chr=c("chr11"), start= c(chr11start),end= c(chr11end)))

chr12data <- toGRanges(
  data.frame(
    chr=c("chr12"), start= c(chr12start),end= c(chr12end)))

chr13data <- toGRanges(
  data.frame(
    chr=c("chr13"), start= c(chr13start),end= c(chr13end)))

chr14data <- toGRanges(
  data.frame(
    chr=c("chr14"), start= c(chr14start),end= c(chr14end)))

chr15data <- toGRanges(
  data.frame(
    chr=c("chr15"), start= c(chr15start),end= c(chr15end)))

chr16data <- toGRanges(
  data.frame(
    chr=c("chr16"), start= c(chr16start),end= c(chr16end)))

chr17data <- toGRanges(
  data.frame(
    chr=c("chr17"), start= c(chr17start),end= c(chr17end)))

chr18data <- toGRanges(
  data.frame(
    chr=c("chr18"), start= c(chr18start),end= c(chr18end)))

chr19data <- toGRanges(
  data.frame(
    chr=c("chr19"), start= c(chr19start),end= c(chr19end)))

chr20data <- toGRanges(
  data.frame(
    chr=c("chr20"), start= c(chr20start),end= c(chr20end)))

chr21data <- toGRanges(
  data.frame(
    chr=c("chr21"), start= c(chr21start),end= c(chr21end)))

chr22data <- toGRanges(
  data.frame(
    chr=c("chr22"), start= c(chr22start),end= c(chr22end)))

chrXdata <- toGRanges(
  data.frame(
    chr=c("chrX"), start= c(chrXstart),end= c(chrXend)))

chrYdata <- toGRanges(
  data.frame(
    chr=c("chrY"), start= c(chrYstart),end= c(chrYend)))

kp <- plotKaryotype(genome="hg38", plot.type=1, main="Density plot for LINE retrotransposons", cex=0.6)

kpAddBaseNumbers(kp)

kpPlotDensity(kp, data= chr1data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr2data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr3data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr4data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr5data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr6data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr7data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr8data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr9data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr10data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr11data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr12data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr13data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr14data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr15data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr16data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr17data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr18data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr19data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr20data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr21data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chr22data, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chrXdata, col="#DBBDED", r0=0, r1=0.5)

kpPlotDensity(kp, data= chrYdata, col="#DBBDED", r0=0, r1=0.5)

kpPlotRegions(kp, data= chrYdata, col="#DBBDED", r0=0, r1=0.5)

