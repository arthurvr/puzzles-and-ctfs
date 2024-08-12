# Toddler's Bottle - cmd1

> Mommy! what is PATH environment in Linux?

Again, let's have look at the source code first. First, the `PATH` environment variable is reset: `PATH=/thankyouverymuch`. Then a filter is applied to limit which commands we can use. The filter consists of some simple `strstr` comparisons, disallowing the use of the words `flag`, `sh` and `tmp`. 

My command below doesn't need anything to be in the `PATH` because it's using the absolute path to `cat`. I circumvent the filter function using printf formatting.
<img width="842" alt="image" src="https://user-images.githubusercontent.com/6025224/251646062-b48c1647-ebe4-4bc6-8d3b-79b57f4bba35.png">
