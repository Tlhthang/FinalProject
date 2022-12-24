import sys
import streamlit as st
from streamlit.web import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "KOL Ranking.py"]
    sys.exit(stcli.main())