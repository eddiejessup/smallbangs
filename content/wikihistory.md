Title: Inspect your Wikipedia browsing history
Date: 2013-09-06
Category: Programming
Tags: Shell, SQL

I was curious to see a chronological list of Wikipedia pages I'd visited. I use Chrome, which stores users' histories in an sqlite database, stored in a OS-dependent location:

- Linux: `~/.config/google-chrome/History`
- Mac: `~/Library/Application Support/Google/Chrome/Default/History`

Once you find this file, I recommend making a copy (`cp History History.bak`) -- as well as being good practice, I think it means you can avoid problems that might arise if Chrome is open while you do all this.

For the next bit you'll need sqlite. You can install it in the usual manner (apt-get for Debian-like linux, brew for mac, etc.).

Now you can run the following command to extract the page titles of all the websites in your history into a file called `history.log`:

```bash
sqlite3 History.bak 'select title from urls;' > history.log
```

It's tempting to make a joke about its embarassing contents, but now that private browsing modes are available in browsers, that seems a bit outdated. Anyway, now we need to do some grepping to find those juicy Wikipedia articles: the following tedious command does the job:

```
cat history.log | grep 'Wikipedia, the free encyclopedia' \
| grep -v -e "(disambiguation)" -e "File:" -e "Talk:" -e "Search results" \
| sed 's_ - Wikipedia, the free encyclopedia__' | uniq | perl -e 'print reverse <>' > wikis.txt
```

This command does this:

1. Scan `history.log` for Wikipedia's characteristic title template
2. Get rid (`grep -v` inverts a pattern match) of pages that aren't really what we're looking for (disambiguation pages, talk pages, image pages, search results)
3. Strip out the Wikipedia title template using sed
4. Remove duplicate entries using uniq
5. Reverse the result so that the most recent pages appear first using perl
6. Redirect the output into a file called `wikis.txt`

(As a side-note, there are more elegant methods to do the reversal, namely `tac` and `tail -r`. However `tac` isn't available by default on OS X, while the `-r` option isn't available for GNU's version of tail. Whereas everybody has perl.)

You should now have a file in your working directory called `wikis.txt`, containing a chronological list of all the Wikipedia pages you've visited since whenever (I've no idea when, if ever, the History database gets archived).

[Here](https://github.com/eddiejessup/Hardtack) is a bash script that should hopefully do all this automatically, though it's a bit of an amateur effort. You can also see there an example file, `wikis_example.txt`, showing the output for my history at the time of writing. To save you time, the most embarassing entry is [arab strap](http://en.wikipedia.org/wiki/Arab_strap_(sexual_device)) (I was looking for the [band](http://en.wikipedia.org/wiki/Arab_Strap_(band))).
