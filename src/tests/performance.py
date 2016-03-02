"""
Use Selenium to Measure Web Timing
Performance Timing Events flow
navigationStart -&gt; redirectStart -&gt; redirectEnd -&gt; fetchStart -&gt; domainLookupStart -&gt; domainLookupEnd
-&gt; connectStart -&gt; connectEnd -&gt; requestStart -&gt; responseStart -&gt; responseEnd
-&gt; domLoading -&gt; domInteractive -&gt; domContentLoaded -&gt; domComplete -&gt; loadEventStart -&gt; loadEventEnd
"""
#import os
#from selenium import webdriver
from selenium import webdriver
from base_test import BaseTest

#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome

class Test_Web_timings2(BaseTest):
    """
     Use Selenium to Measure Web Timing
     Performance Timing Events flow
     navigationStart -> redirectStart -> redirectEnd -> fetchStart -> domainLookupStart -> domainLookupEnd 
      -> connectStart -> connectEnd -> requestStart -> responseStart -> responseEnd 
      -> domLoading -> domInteractive -> domContentLoaded -> domComplete -> loadEventStart -> loadEventEnd
    """
    #from selenium import webdriver
    
    def test_webtimings(self): 
        source = "http://www.babycenter.com/"
        driver = webdriver.Chrome()
        driver.get(source)
        
        navigationStart = driver.execute_script("return window.performance.timing.navigationStart")    
        responseStart = driver.execute_script("return window.performance.timing.responseStart")
        domComplete = driver.execute_script("return window.performance.timing.domComplete")
        
        backendPerformance = responseStart - navigationStart
        frontendPerformance = domComplete - responseStart
        
        print "Back End: %s" % backendPerformance
        print "Front End: %s" % frontendPerformance
        
        #driver.quit()

    

