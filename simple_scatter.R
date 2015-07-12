library(foreign)
library(ggplot2)
library(sandwich)

#URLs data from Chris
setwd("/Users/christinezhang/Desktop/Hackathon2015_WashingtonPost")
list.files()
urls <- read.csv('urls.csv')
urls <- urls[order(-urls$visit_count), ]
View(urls)

urls$l.comment <- log(urls$comment_count)
urls$l.visit <- log(urls$visit_count)

ggplot(urls[urls$l.comment > 0 & urls$l.visit > 0 ,], aes(x = l.visit, y = l.comment)) + 
  geom_point(color = 'darkblue')+
  geom_line(stat='smooth')+
  theme_bw()+
  xlab("")+
  ylab("")+
  theme(axis.text = element_blank(), axis.ticks = element_blank())
  
ggsave('scatter.png', width=8)

summary(m1 <- glm(comment_count ~ visit_count, family="poisson", data= urls))
cov.m1 <- vcovHC(m1, type="HC0")
std.err <- sqrt(diag(cov.m1))
r.est <- cbind(Estimate= coef(m1), "Robust SE" = std.err,
               "Pr(>|z|)" = 2 * pnorm(abs(coef(m1)/std.err), lower.tail=FALSE),
               LL = coef(m1) - 1.96 * std.err,
               UL = coef(m1) + 1.96 * std.err)

r.est # poisson regression example

# other data file - from newswhip.json
dat1 <- read.csv("data_1_2966.csv")
names(dat1)
dat1.short <- dat1[, c(2,8:32)]

dat2 <- read.csv("data_2_rest.csv")
names(dat2)
dat2.short <- dat2[, c(2,8:32)]

dat <- rbind(dat1.short, dat2.short)
head(dat)
names(dat)
dat$count <- 1
str(dat)
dat.agg <- aggregate(dat$count, by= list(dat$articles.0.topics.0.name), sum)
dat.agg <- dat.agg[order(-dat.agg$x), ]
colnames(dat.agg) <- c('topic','count')
dat.agg.10 <- head(dat.agg, 10)

dat.agg.10$cat <- factor(dat.agg.10$topic, as.character(dat.agg.10$topic))
dat.agg.10
ggplot(dat.agg.10[dat.agg.10$cat!='', ], aes(x = cat, y = count))+
  geom_bar(stat = 'identity')

dat <- dat[order(-dat$articles.0.fb_data.share_count), ]
View(dat[dat$articles.0.fb_data.share_count>0, ])
names(dat)
dat <- dat[dat$articles.0.publication_timestamp>1427126160000,]
write.csv(dat, 'dat.csv')
table(dat$articles.0.publication_timestamp)

names(dat)
dat.10 <- head(dat, 10)
dat$ratio = dat$articles.0.fb_data.like_count/dat$articles.0.fb_data.share_count
dat$l.like <- log(dat$articles.0.fb_data.like_count)
dat$l.share <- log(dat$articles.0.fb_data.share_count)


ggplot(dat[dat$articles.0.fb_data.share_count>0 & dat$articles.0.fb_data.like_count>0, ], aes(x = l.share, y = l.like))+
  geom_point()

dat2 <- dat[order(-dat$articles.0.tw_data.tw_count), ]
View(dat2)


dat3 <- dat[order(-dat$articles.0.li_data.li_count), ]
View(dat3)

