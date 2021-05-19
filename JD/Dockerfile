FROM noobx/jd:gitee

RUN cd $JD_DIR \
    && git remote set-url origin https://github.com/DovFork/jd-base \
    && git fetch \
    && git reset --hard origin/master \
    && cd $JD_DIR/panel && npm install \
    && cd $JD_DIR/scripts \
    && git remote set-url origin https://github.com/DovFork/jd-scripts \
    && git fetch \
    && git reset --hard origin/master \
    && npm install