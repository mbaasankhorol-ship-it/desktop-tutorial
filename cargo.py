import streamlit as st
import backend as be
import pandas as pd
import json
import requests
from datetime import datetime, timedelta


st.header("📦 Карго тооцоолуур")

# 1. Өндөр (Тоо + Нэгж)
col_h1, col_h2 = st.columns([3, 1]) # 3:1 харьцаатай (Тоо нь том, нэгж нь жижиг)
with col_h1:
    h_val = st.number_input("Өндөр", value=10.0, key="h_val")
with col_h2:
    h_unit = st.selectbox("Нэгж", ["см", "м"], key="h_unit")

# 2. Гүн (Тоо + Нэгж)
col_d1, col_d2 = st.columns([3, 1])
with col_d1:
    d_val = st.number_input("Гүн", value=10.0, key="d_val")
with col_d2:
    d_unit = st.selectbox("Нэгж", ["см", "м"], key="d_unit", label_visibility="collapsed")

# 3. Урт (Тоо + Нэгж)
col_l1, col_l2 = st.columns([3, 1])
with col_l1:
    l_val = st.number_input("Урт", value=10.0, key="l_val")
with col_l2:
    l_unit = st.selectbox("Нэгж", ["см", "м"], key="l_unit", label_visibility="collapsed")

# 4. Жин (Тоо + Нэгж)
col_w1, col_w2 = st.columns([3, 1])
with col_w1:
    w_val = st.number_input("Жин", value=1.0, key="w_val")
with col_w2:
    w_unit = st.selectbox("Нэгж", ["кг", "гр"], key="w_unit", label_visibility="collapsed")

# --- ХӨРВҮҮЛЭХ ЛОГИК ---
# Бүгдийг нь СМ болон КГ руу шилжүүлнэ
h_cm = h_val * 100 if h_unit == "м" else h_val
d_cm = d_val * 100 if d_unit == "м" else d_val
l_cm = l_val * 100 if l_unit == "м" else l_val
w_kg = w_val / 1000 if w_unit == "гр" else w_val

if st.button("🚀 Тооцоолох"):
    price = be.cargo_price_calculator(h_cm, d_cm, l_cm, w_kg)
    st.success(f"💰 Каргоны үнэ: {price:,.0f} ₮")
