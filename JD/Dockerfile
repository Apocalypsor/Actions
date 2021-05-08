FROM noobx/jd:gitee

RUN cd $JD_DIR \
    && git remote set-url origin https://github.com/DovFork/jd-base \
    && git pull && git reset --soft origin/master \
    cd $JD_DIR/scripts \
    && git remote set-url origin https://github.com/DovFork/jd-scripts \
    && git pull && git reset --soft origin/master \