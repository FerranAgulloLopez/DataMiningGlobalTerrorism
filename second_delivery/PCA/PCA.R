dd <- read.csv("fips-codes-added.csv")
#In order to do PCA the data must not have any NA's so we replace NA with
#the value of their medians.
dd$nkillter[which(is.na(dd$nkillter))] <- 0
dd$nwoundus[which(is.na(dd$nwoundus))] <- 0
dd$nwoundte[which(is.na(dd$nwoundte))] <- 0


#set a list of numerical variables

dcon <- data.frame (dd$nkill,dd$nkillus,dd$nkillter,dd$nwound,dd$nwoundus,dd$nwoundte)

# PRINCIPAL COMPONENT ANALYSIS OF dcon

pc1 <- prcomp(dcon, scale=TRUE)
class(pc1)
attributes(pc1)

print(pc1)
#PC1 = Sangría, PC2 = Heridos no muertos civiles (Cuanto se salvó la gente), PC3 = Terroristas heridos *-1
# WHICH PERCENTAGE OF THE TOTAL INERTIA IS REPRESENTED IN SUBSPACES?
pc1$sdev
inerProj<- pc1$sdev^2 
inerProj
totalIner<- sum(inerProj)
totalIner
pinerEix<- 100*inerProj/totalIner
pinerEix
barplot(pinerEix)

#Cummulated Inertia in subspaces, from first principal component to the 11th dimension subspace
barplot(100*cumsum(pc1$sdev[1:dim(dcon)[2]]^2)/dim(dcon)[2])
percInerAccum<-100*cumsum(pc1$sdev[1:dim(dcon)[2]]^2)/dim(dcon)[2]
percInerAccum

# SELECTION OF THE SINGIFICNT DIMENSIONS (keep 80% of total inertia)

nd = 3

# STORAGE OF THE EIGENVALUES, EIGENVECTORS AND PROJECTIONS IN THE nd DIMENSIONS


Psi = pc1$x[,1:nd]

# STORAGE OF LABELS FOR INDIVIDUALS AND VARIABLES

iden = row.names(dcon)
etiq = names(dcon)
ze = rep(0,length(etiq)) # WE WILL NEED THIS VECTOR AFTERWARDS FOR THE GRAPHICS

# PLOT OF INDIVIDUALS

#select your axis
eje1<-1
eje2<-2
eje3<-3

plot(Psi[,eje1],Psi[,eje2])
#text(Psi[,eje1],Psi[,eje2],labels=iden, cex=0.5)
axis(side=1, pos= 0, labels = F, col="red")
axis(side=3, pos= 0, labels = F, col="red")
axis(side=2, pos= 0, labels = F, col="red")
axis(side=4, pos= 0, labels = F, col="red")

plot(Psi[,eje1],Psi[,eje3])
axis(side=1, pos= 0, labels = F, col="red")
axis(side=3, pos= 0, labels = F, col="red")
axis(side=2, pos= 0, labels = F, col="red")
axis(side=4, pos= 0, labels = F, col="red")

plot(Psi[,eje2],Psi[,eje3])
axis(side=1, pos= 0, labels = F, col="red")
axis(side=3, pos= 0, labels = F, col="red")
axis(side=2, pos= 0, labels = F, col="red")
axis(side=4, pos= 0, labels = F, col="red")


if(!require(rgl))install.packages("rgl"); require(rgl)
library(rgl)
plot3d(Psi[,1],Psi[,2],Psi[,3])

#Projection of variables

Phi = cor(dcon,Psi)

#select your axis

X<-Phi[,eje1]
Y<-Phi[,eje2]
Z<-Phi[,eje3]


#zooms
plot(Psi[,eje1],Psi[,eje2],type="n",xlim=c(min(X,0),max(X,0)))
axis(side=1, pos= 0, labels = F)
axis(side=3, pos= 0, labels = F)
axis(side=2, pos= 0, labels = F)
axis(side=4, pos= 0, labels = F)
arrows(ze, ze, X, Y, length = 0.07,col="red")
text(X,Y,labels=etiq,col="blue", cex=0.7)

#Now we project both cdgs of levels of a selected qualitative variable without
#representing the individual anymore

plot(Psi[,eje1],Psi[,eje2],type="n",xlim=c(-1,13))
axis(side=1, pos= 0, labels = F, col="gray")
axis(side=3, pos= 0, labels = F, col="gray")
axis(side=2, pos= 0, labels = F, col="grey")
axis(side=4, pos= 0, labels = F, col="grey")

#select your qualitative variable
k<-19#weaptype
varcat<-dd[,k]
fdic1 = tapply(Psi[,eje1],varcat,mean)
fdic2 = tapply(Psi[,eje2],varcat,mean) 

points(fdic1,fdic2,pch=16,col="blue", labels=levels(varcat))
text(fdic1,fdic2,labels=levels(varcat),col="blue", cex=0.7)


#all qualitative together
plot(Psi[,eje1],Psi[,eje2],type="n",xlim=c(-0.5,1.5),ylim=c(-0.5,1.5))
axis(side=1, pos= 0, labels = F, col="gray")
axis(side=3, pos= 0, labels = F, col="gray")
axis(side=2, pos= 0, labels = F, col="gray")
axis(side=4, pos= 0, labels = F, col="gray")

#nominal qualitative variables

dcat<-c(10,11,12,17,18,19,29,30)
#divide categoricals in several graphs if joint representation saturates

#build a palette with as much colors as qualitative variables 

#colors<-c("blue","red","green")
#alternative
colors<-rainbow(length(dcat))

c<-1
for(k in dcat){
  seguentColor<-colors[c]
  fdic1 = tapply(Psi[,eje1],dd[,k],mean)
  fdic2 = tapply(Psi[,eje2],dd[,k],mean) 
  
  points(fdic1,fdic2,pch=16,col=seguentColor)
  #text(fdic1,fdic2,labels=levels(dd[,k]),col=seguentColor, cex=0.6)
  c<-c+1
}
legend("topright",names(dd)[dcat],pch=1,col=colors, cex=0.6)

#determine zoom level
#use the scale factor or not depending on the position of centroids
# ES UN FACTOR D'ESCALA PER DIBUIXAR LES FLETXES MES VISIBLES EN EL GRAFIC
#fm = round(max(abs(Psi[,1]))) 
#fm=100

#scale the projected variables
#X<-fm*Psi[,eje1]
#Y<-fm*Psi[,eje2]

#represent numerical variables in background
#plot(Psi[,eje1],Psi[,eje2],type="n",xlim=c(-1,1), ylim=c(-3,1))
#plot(X,Y,type="none",xlim=c(min(X,0),max(X,0)))
#axis(side=1, pos= 0, labels = F, col="cyan")
#axis(side=3, pos= 0, labels = F, col="cyan")
#axis(side=2, pos= 0, labels = F, col="cyan")
#axis(side=4, pos= 0, labels = F, col="cyan")

#add projections of numerical variables in background
#arrows(ze, ze, X, Y, length = 0.07,col="lightgray")
#text(X,Y,labels=etiq,col="gray", cex=0.7)

#add centroids
#c<-1
#for(k in dcat){
#  seguentColor<-colors[c]
#  
#  fdic1 = tapply(Psi[,eje1],dd[,k],mean)
#  fdic2 = tapply(Psi[,eje2],dd[,k],mean) 
#  
#  points(fdic1,fdic2,pch=16,col=seguentColor, labels=levels(dd[,k]))
#  #text(fdic1,fdic2,labels=levels(dd[,k]),col=seguentColor, cex=0.6)
#  c<-c+1
#}
#legend("topright",names(dd)[dcat],pch=1,col=colors, cex=0.6)

# PROJECTION OF ILLUSTRATIVE qualitative variables on individuals' map
# PROJECCIÓ OF INDIVIDUALS DIFFERENTIATING THE Dictamen
# (we need a numeric Dictamen to color)

varcat=dd[,29]
plot(Psi[,1],Psi[,2],col=varcat,xlim=c(-1,20), ylim=c(-3,20))
axis(side=1, pos= 0, labels = F, col="darkgray")
axis(side=3, pos= 0, labels = F, col="darkgray")
axis(side=2, pos= 0, labels = F, col="darkgray")
axis(side=4, pos= 0, labels = F, col="darkgray")
legend("topright",levels(varcat),pch=1,col=c(1,2), cex=0.6)

varcat=dd[,10]
plot(Psi[,1],Psi[,2],col=varcat,xlim=c(-1,20), ylim=c(-3,20))
axis(side=1, pos= 0, labels = F, col="darkgray")
axis(side=3, pos= 0, labels = F, col="darkgray")
axis(side=2, pos= 0, labels = F, col="darkgray")
axis(side=4, pos= 0, labels = F, col="darkgray")
legend("topright",levels(varcat),pch=1,col=c(1,2), cex=0.6)


# Overproject THE CDG OF  LEVELS OF varcat
#fdic1 = tapply(Psi[,1],varcat,mean)
#fdic2 = tapply(Psi[,2],varcat,mean) 

#text(fdic1,fdic2,labels=levels(varcat),col="cyan", cex=0.75)
