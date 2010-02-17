import datetime
begin=datetime.datetime.now()
import os, sys, re
import md2html


#
# TODO: delete files in html that are not in src.
#
#
#

def usage():
    print"""
    usage: python Makefile.py [-f] <sourcedir> <targetdir>
    
        sourcedir: directory structure with markdown files
        targetdir: writable directory for the html files
        
        -f      Force remake, ignoring file timestamps
    """


def make(search_path, write_path, forced=False):    
    if forced:
        print("== Forced remake\n")
    
    
    madestuff=False
    for path, subdirs, files in os.walk(search_path):
        #something smells here:
        targetdir=re.sub("src", "html", os.path.abspath(os.path.relpath(path, write_path)))
        path=os.path.abspath(path)
        
        #if targetdir does not exist, create dir
        if not os.path.isdir(targetdir) and not os.path.isfile(targetdir):
            os.mkdir(targetdir)
        
        
        for filename in files:
            do_make = False
            sourcefile=os.path.join(path, filename)
            if filename[-3:]==".md":
                targetfile=os.path.join(targetdir, filename[:-3]+".html")
                if os.access(targetfile, os.F_OK):
                    if os.access(targetfile, os.R_OK|os.W_OK):
                        if os.lstat(sourcefile).st_mtime > os.lstat(targetfile).st_mtime:
                            print "Target older than source:"
                            do_make=True
                    else:
                        print("[FATAL]: Read/write presmission failure on target: %s"%targetfile)
                else:
                    print("Target does not exist.")
                    do_make=True
                
                if do_make or forced:
                    madestuff=True
                    try:
                        print("Making".ljust(10)+targetfile+"\nfrom".ljust(10)+sourcefile+"\n")
                        #print "Making".ljust(10)+filename.ljust(20)+"->".ljust(10)+filename[:-3]+".html"
                        open(targetfile,"w").write(md2html.convert(open(sourcefile, "r").read()))
                    except AttributeError:
                        print "\t[Error]: Making '%s' from '%s'. Check source file syntax. Ignoring source."%(targetfile, sourcefile)
    return madestuff
    
if __name__=="__main__":
    try:
        if sys.argv[1] != "-f":
            sourcedir=sys.argv[1]
            targetdir=sys.argv[2]
            is_forced=False
        else:
            sourcedir=sys.argv[2]
            targetdir=sys.argv[3]
            is_forced=True
    except IndexError:
        usage()
        sys.exit()

    print "== Begin website make =="
    print ""
    if not os.access(sourcedir, os.R_OK|os.W_OK):
        print "'%s' could not be read or '%s' could not be written to. Exiting."%(sourcedir, targetdir)
        sys.exit()
    donestuff = make(sourcedir,targetdir, forced= is_forced)
    if not donestuff:
        print("All files up to date, nothing done.")
    end=datetime.datetime.now()
    print ""
    print "== time taken: "+str(end-begin)+" =="
    
