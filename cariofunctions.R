localization <- function(chr,gstart,gend,png) {
  
  library(crop)
  library(karyoploteR)
  
  chrs <- toGRanges(
    data.frame(
      chr=chr, start= gstart,end= gend))
  
  png(filename = png, bg = "transparent", res = 120)
  kp <- plotKaryotype(genome="hg38", plot.type=4, chromosomes=chr)
  kpAddBaseNumbers(kp)
  kpDataBackground(kp, r0=0, r1=0.05, color = "gray77", data.panel = 2)
  kpPlotRegions(kp, data=chrs, col="orchid4", r0=0, r1=0.1)
  dev.off.crop(file=png)
  return()
  
}

zoom <- function(chr,gstart,gend,png) {
  
  zoom1 <- gstart - 10000000
  zoom2 <- gend + 10000000
  
  library(crop)
  library(karyoploteR)
  
  chrs <- toGRanges(
    data.frame(
      chr=chr, start= gstart,end= gend))
  
  detail.region <- toGRanges(data.frame(chr, zoom1, zoom2))
  
  png(filename = png, bg = "transparent", res = 120)
  kp <- plotKaryotype(genome="hg38", plot.type=4, zoom = detail.region)
  kpAddBaseNumbers(kp, tick.dist=1000000)
  kpDataBackground(kp, r0=0, r1=0.05, color = "gray77", data.panel = 2)
  kpPlotRegions(kp, data=chrs, col="orchid4", r0=0, r1=0.1)
  dev.off.crop(file=png)
  return()
  
}





