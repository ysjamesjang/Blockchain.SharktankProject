# Initializing imports.
from pathlib import Path
import pandas as pd
import numpy as np
import datetime as dt
import streamlit as st
pd.set_option('display.max_colwidth', None)

st.sidebar.title("GET FUNDING")

st.title("Shark Tank Smart Contract Marketplace")

st.write("Are you in need of funding for your next project or venture? The Shark Tank Marketplace is your place to find funding. From a single investor or a bunch of small investors, the Shark Tank Marketplace utilizes Smart Contracts to secure future deals in stone on the blockchain.")

st.markdown("---")

st.sidebar.text_input('Input your Company Name here:')

st.sidebar.text_input('Input your company webpage here:')

st.sidebar.text_input('Input your company slogan or pitch here:')

st.sidebar.text_input('Input details about your company here:')

st.sidebar.slider("How much money are you looking to raise?", 1000,1000000)

st.sidebar.slider("How much equity percentage (%) are you providing to the investors?", 1,100)

st.title("START INVESTING")

st.title("For investors")

st.level3 = st.slider("How much money are you looking to invest?", 1000,1000000)

# Creating a list of companies and assigning to a dataframe. Companies found on https://startupschicago.net/.
Companies = {'Company': ['Parser.run'
                         , 'CancerIQ'
                         , 'Invitation codes'
                         , 'YCharts'
                         , 'Groupon'
                         , 'EVENTup'
                         , 'ParkWhiz'
                         , 'Food Genius'
                         , 'OpenAirplane'
                         , 'GiveForward'
                         , 'Rocketmiles'
                         , 'Classkick'
                         , 'Shortlist'
                         , 'Narrative Science'
                         , 'Packback'
                         , 'Storymix Media'
                         , 'Opternative'
                         , 'Shiftgig'
                         , 'Visible'
                         , 'Fooda'
                         , 'Cloudbot'
                         , 'Raise'
                         , 'FourKites'
                         , 'Sprout Social'
                         , 'SpotHero']}
companies_df = pd.DataFrame(data=Companies)

# Creating a list which provides the company's pitch or slogan then building another dataframe.
ShortDescription = {'Slogan/Pitch': ['We extract data from websites.'
                               , 'Using Genetic Information to Predict, Pre-empt, and Prevent Cancer.'
                               , 'The referral community.'
                               , 'The Financial Terminal of The Web.'
                               , 'Daily Deals. Delivered.'
                               , 'Largest online marketplace for Event Spaces.'
                               , 'Click here. Park anywhere.'
                               , 'Feeding the foodservice Industry smarter data and analytics.'
                               , 'Making renting an airplane as easy as renting a car.'
                               , 'Crowdfunding for medical and life events.'
                               , 'Fueling more vacations.'
                               , 'Students Learn Together.'
                               , 'LinkedIn for your event life.'
                               , 'The leader in automated narrative generation for the enterprise.'
                               , 'Fearlessly curious.'
                               , 'Turning photos and footage into amazing custom edited videos'
                               , 'The First Online Eye Exam'
                               , 'Transforming the Way People Work.'
                               , 'Your investor relationship hub.'
                               , 'Food at work: powered by local restaurants, loved by employees'
                               , 'Your apps. Simplified.'
                               , 'Save more everywhere you shop.'
                               , 'Real-Time Visibility for Your Entire Supply Chain'
                               , 'Reimagine the role of social in your business'
                               , 'Find and Book Parking in Seconds.']}
short_description_df = pd.DataFrame(data=ShortDescription)

# Creating a list which provides the company's background or specialty then assigning to another dataframe.
LongDescription = {'About': ['Simple, custom web scraping tools for researchers, growth hackers, marketing & sales teams.'
                             , 'Our team has modeled proven cancer genetics workflows at top academic centers, and translated them into a suite of digital health tools. ancerIQ helps leading health systems maximize the clinical and financial value of using genetics in routine care. Together we can help to detect and prevent the deadliest and earliest onset cancers.'
                             , 'Invitation is the place for referral codes. Invitation App is a social network where people post their referral codes and collect rewards on autopilot.'
                             , 'YCharts is a financial software company that was founded in 2009 and is backed by Morningstar. YCharts provides the analytic power of a financial terminal (such as Bloomberg, FactSet, CapIQ), but with the ease of use and accessibility of a modern website.'
                             , 'Groupon features a daily deal on the best stuff to do, see, eat, and buy in 45 countries, and soon beyond. We have about 10,000 employees working across our Chicago headquarters, a growing office in Seattle and Palo Alto, CA. Groupon is a place where customers can discover new experiences every day and local businesses thrive.'
                             , 'Eventup is a marketplace that allows consumers to find both commercial venues and unique residential properties and book them for their event. We make the venue selection and booking process easier and provide access to experiences that were previously unattainable.'
                             , 'ParkWhiz simplifies the parking experience by facilitating the advance purchase of parking for any driving occasion. Available on any device -- PC, tablet, or smartphone -- ParkWhiz features parking options and deals at over 1,500 locations nationwide.'
                             , 'We’re feeding the Foodservice Industry smarter data and analytics. Food Genius is a leading foodservice data provider specializing in gathering, preparing, and serving granular foodservice menu data and analytics. Food Genius supports foodservice manufacturers.'
                             , 'We’re making a pilot certificate more useful. OpenAirplane makes it easy for Pilots to find, book, fly, and pay for aircraft rental online or with a mobile device. We’re helping Operators get better utilization of their fleets, and Pilots fly more.'
                             , 'GiveForward lets anyone to create a free fundraising page for a friend or loved one’s uncovered medical bills, memorial fund, adoptions or any other life events in five minutes or less. Millions of families have used GiveForward to raise more than $165M.'
                             , 'We enable our customers to travel more, travel better and travel further. 20M+ consumers stock away miles & points to satisfy their wanderlust. Flying around or using credit cards are the only good ways to fill the stockpile today. We’ve built the third way. Book hotels, get rewarded. Earn thousands of miles or points per night from your favorite loyalty programs.'
                             , 'Numbers - Launched fall 2014 - 150K downloads - Average 30% wk/wk growth - 50 states / 70 countries - 45K questions answered/week - Engine of growth: 65% of signups are word-of-mouth, 100% are organic, $0 spent marketing Created by teachers and engineers, Classkick: Helping Teachers Be Awesome. See all your students working and give high-quality feedback–from anywhere.'
                             , 'Shortlist connects you with the people you don’t know—but should—at conferences and trade shows. Our mobile-social platform "accelerates serendipity" to maximize everyone’s time and opportunity. Brands pay us to sponsor the app for their target events. The smartest, fastest way to manage your freelance workforce. Onboard, assign, and pay your freelancers from a single, user-friendly platform.'
                             , 'Powered by artificial intelligence, Narrative Science Quill™ is an advanced natural language generation platform for the enterprise that creates data-driven communications at machine scale. It analyzes data from disparate sources and understands relationships hidden. No more dashboards. Bring data insights to everyone in your company in a way they actually understand with Data Storytelling in Lexio.'
                             , 'Pay-per-use etextbooks for $5 or less. Packback allows college students to "pay per use" for their digital textbooks by renting for $3-$5 per day, while enabling publishers to recoup revenue lost to the secondary used book market. Any money students spend on daily rentals can be directly converted towards an extended semester or year-long rental of that same digital title. Packback is a different kind of online discussion that teaches students how to ask effective, open-ended questions. Inspire self-motivated, critical thinkers through inquiry-driven discussion.'
                             , 'Millions of videos are taken at events like your child’s soccer game, SXSW, or the CES. Yet 99% of those videos are never seen, much less transformed into something of value. Enter VideoStitch. Easily crowdsource and access the video clips and photos from everyone. Crowdsourced content and automated video creation platform.'
                             , 'Opternative’s mission is to help the world see and feel better. Opternative has developed the first online eye exam that delivers a prescription, signed by an ophthalmologist, for glasses and contact lenses. The exam takes 15 minutes. The quickest way to renew your prescription. Get your eyes checked and renew your vision prescription from the comfort of your home.'
                             , 'Shiftgig provides staffing agencies with on-demand staffing software to grow and scale their business. Our software solutions empower your workforce with flexibility and choice while allowing you to deliver powerful strategic insights to your clients. Shiftgig is the service industry community, a platform that allows employers and candidates to show needs, skills, and availability to connect more efficiently. Launched in early 2012, over 100,000 service industry people 4,000 businesses have connected.'
                             , 'Update investors, raise capital and track metrics from a single platform. Data sharing for startups and their investors. Visible simplifies the sharing, management, and reporting of data between startups and investors. Visible was launched by a group of founders and investors that had been struggling with the vexing, but all too common, problems of tracking investment performance.'
                             , 'Fooda is a food technology platform that connects restaurants to people while at work. Companies and individuals join Fooda to get food brought right to their office everyday.'
                             , 'Helping you maintain your relationships across multiple networks through a social address book and unified inbox. Cloudbot is a mobile and web application that is an efficient solution to having your personal data and relationships scattered around on different services. People rely on different applications to access the little bits of their lives saved in the cloud.'
                             , 'Changing the World of Gift Cards - Incentive Marketing, Brand Enterprise Software & Beyond. Raise is a C2C gift card marketplace where members can sell gift cards for cash or save on gift cards to their favorite stores. Raise helps buyers increase their purchase power and allows sellers to raise their earning potential. Unlock discounted and cash back gift cards, coupons, and today’s best offers with Raise.'
                             , 'Enterprise Cloud for Logistics and Supply Chain Management. FourKites is reinventing the complex and labor intensive communication systems in the Logistics and Transportation Industry by providing a cost-effective, real-time and easy-to-use cloud based software solution. The #1 Global Supply Chain Visibility Platform, trusted by the world’s most recognized brands, including Coca-Cola, Walmart, Dow and many more.'
                             , 'Sprout is a social media management platform used by leading companies across the globe. Sprout’s Social Media Management platform is used by thousands of leading countries around the world to more effectively manage social channels, audience engagement, social relationship management and reporting/analytics.'
                             , 'SpotHero is an on-demand app for parking that allows drivers to reserve their perfect spot right from the web and their phones. We partner with garages, lots and valets to get drivers discounted parking spots all across the US.']}
long_description_df = pd.DataFrame(data=LongDescription)

# Creating a list for each company's website and building another dataframe.
WebAddress = {'Website': ['https://parser.run/'
                          , 'https://www.canceriq.com/'
                          , 'https://invitation.codes/'
                          , 'https://ycharts.com/'
                          , 'https://www.groupon.com/'
                          , 'https://eventup.com/'
                          , 'https://www.parkwhiz.com/'
                          , 'https://getfoodgenius.com/'
                          , 'https://www.openairplane.com/'
                          , 'https://www.giveforward.com/'
                          , 'https://www.rocketmiles.com/rm/home/en/'
                          , 'https://classkick.com/'
                          , 'https://getshortlist.com/'
                          , 'https://narrativescience.com/'
                          , 'https://www.packback.co/'
                          , 'https://www.storymixmedia.com/'
                          , 'https://govisibly.com/lite-site/opternative/'
                          , 'https://www.shiftgig.com/'
                          , 'https://www.visible.vc/'
                          , 'https://www.fooda.com/'
                          , 'http://cloudbot.com/'
                          , 'https://www.raise.com/'
                          , 'https://www.fourkites.com/'
                          , 'https://sproutsocial.com/'
                          , 'https://spothero.com/']}
website_df = pd.DataFrame(data=WebAddress)

# Using random numbers to assign the capital each company is looking to raise.
data_1 = np.random.randint(10000,500000, size=25)
capital_df = pd.DataFrame(data_1, columns=['Capital Seeking in USD']).round(-4)

# Using random numbers to assign the equity each company is looking to offer.
data_2 = np.random.randint(5,35, size=25)
stake_df = pd.DataFrame(data_2, columns=['% Equity Stake'])

# Converting interger to a decimal.
valuation_decimal = stake_df*0.01

# Calculating the valuation of each company by dividing the amount of capital each company is seeking by the % equity they are looking to give up.
valuation_df = capital_df['Capital Seeking in USD']/valuation_decimal['% Equity Stake']

# Converting from series to a dataframe and each value to an interger.
valuation_df = valuation_df.to_frame().astype(int)

# Naming the valuation dataframe and rounding.
valuation_df = valuation_df.rename(columns={0 : 'Approx. Company Valuation in USD'}).round(-3)

# Randomly generating the rating score and rounding to the nearest tenths.
data_3 = np.random.uniform(3.5,5.0, size=25)
rating_df = pd.DataFrame(data_3, columns=['Business Rating']).round(1)

# Concatinating all individual dataframes to a single dataframe.
concatenated = pd.concat([companies_df, short_description_df, long_description_df, website_df, capital_df, stake_df, valuation_df, rating_df], axis=1)

# Creating a dictionary for the investors and their expertise.
investors = {'Anonymous Investor A' : 'Sales/Marketing/Merchandising'
             , 'Anonymous Investor B' : 'Manufacturing/Distribution'
             , 'Anonymous Investor C' : 'Technology'
             , 'Anonymous Investor D' : 'Supply Chain/Logistics'
             , 'No Investors' : 'Open'}

# Randomly assigning investors to businesses which they will invest in.
concatenated['Investor'] = np.random.choice(list(investors),len(concatenated))
concatenated['Investor Network & Expertise'] = concatenated['Investor'].map(investors)

option = st.selectbox("Please select a company you would like to invest in.",sorted(concatenated['Company'].unique()))

st.markdown("---")

st.subheader(concatenated[concatenated['Company']==option]['Company'].iloc[0])

st.markdown('**Pitch/Slogan**')

st.write(concatenated[concatenated['Company']==option]['Slogan/Pitch'].iloc[0])

st.markdown('**About**')

st.write(concatenated[concatenated['Company']==option]['About'].iloc[0])

st.markdown('**Website**')

st.write(concatenated[concatenated['Company']==option]['Website'].iloc[0])

st.markdown('**Capital Seeking (USD)**')

st.write(concatenated[concatenated['Company']==option]['Capital Seeking in USD'].iloc[0])

st.markdown('**Equity Stake (%)**')

st.write(concatenated[concatenated['Company']==option]['% Equity Stake'].iloc[0])

st.markdown('**Approx. Company Valuation (USD)**')

st.write(concatenated[concatenated['Company']==option]['Approx. Company Valuation in USD'].iloc[0])

st.markdown('**Business Rating**')

st.write(concatenated[concatenated['Company']==option]['Business Rating'].iloc[0])

st.markdown('**Investor**')

st.write(concatenated[concatenated['Company']==option]['Investor'].iloc[0])

st.markdown('**Investor(s) Network & Expertise**')

st.write(concatenated[concatenated['Company']==option]['Investor Network & Expertise'].iloc[0])