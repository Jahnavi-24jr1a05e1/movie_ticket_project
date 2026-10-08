import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Movie Ticket Booking",
    page_icon="🎬",
    layout="centered"
)

st.markdown("""
<style>
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.total {
    font-size: 30px;
    font-weight: bold;
    text-align: center;
}

.poster-title {
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🎬 Movie Ticket Booking</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Book your favorite movie tickets easily 🍿</div>',
    unsafe_allow_html=True
)

st.markdown("---")

movies = {
    "Avengers: Endgame": {
        "price": 200,
        "poster": "posters/avengers.jpg"
    },
    "Leo": {
        "price": 180,
        "poster": "posters/leo.jpg"
    },
    "RRR": {
        "price": 220,
        "poster": "posters/rrr.jpg"
    },
    "Paradise": {
        "price": 200,
        "poster": "posters/paradise.jpg"
    },
    "Interstellar": {
        "price": 250,
        "poster": "posters/interstellar.jpg"
    },
    "Kalki 2898 AD": {
        "price": 220,
        "poster": "posters/kalki.jpg"
    }
}

ticket_prices = {
    "Regular": 150,
    "Premium": 250,
    "VIP": 400
}

st.subheader("🎥 Select Your Movie")

movie = st.selectbox(
    "Choose a movie",
    list(movies.keys())
)

col1, col2 = st.columns([1, 1.5])

with col1:
    st.image(
        movies[movie]["poster"],
        width=250
    )

with col2:
    st.markdown(
        f'<div class="poster-title">🎬 {movie}</div>',
        unsafe_allow_html=True
    )

    st.write("")
    st.write(f"🎟️ Movie Base Price: ₹{movies[movie]['price']}")
    st.write("🍿 Enjoy the ultimate movie experience!")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎟️ Ticket Type")

    ticket_type = st.selectbox(
        "Select ticket type",
        list(ticket_prices.keys())
    )

with col2:
    st.subheader("👥 Number of Tickets")

    tickets = st.number_input(
        "How many tickets?",
        min_value=1,
        max_value=10,
        value=1,
        step=1
    )

st.markdown("---")

st.subheader("📅 Booking Details")

col1, col2 = st.columns(2)

with col1:
    booking_date = st.date_input(
        "Select Date"
    )

with col2:
    show_time = st.selectbox(
        "Select Show Time",
        [
            "10:00 AM",
            "1:00 PM",
            "4:00 PM",
            "7:00 PM",
            "10:00 PM"
        ]
    )

st.markdown("---")

movie_price = movies[movie]["price"]
ticket_price = ticket_prices[ticket_type]

price_per_ticket = movie_price + ticket_price
subtotal = price_per_ticket * tickets

gst = subtotal * 0.05
grand_total = subtotal + gst

if st.button(
    "🎟️ Confirm Booking",
    use_container_width=True
):

    st.balloons()

    st.success("🎉 Booking Confirmed Successfully!")

    st.markdown("## 🧾 Booking Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.write("🎬 **Movie**")
        st.write("🎟️ **Ticket Type**")
        st.write("👥 **Number of Tickets**")
        st.write("📅 **Booking Date**")
        st.write("🕐 **Show Time**")
        st.write("💰 **Price Per Ticket**")
        st.write("🧾 **Subtotal**")
        st.write("💸 **GST (5%)**")

    with col2:
        st.write(movie)
        st.write(ticket_type)
        st.write(tickets)
        st.write(booking_date.strftime("%d-%m-%Y"))
        st.write(show_time)
        st.write(f"₹{price_per_ticket:.2f}")
        st.write(f"₹{subtotal:.2f}")
        st.write(f"₹{gst:.2f}")

    st.markdown("---")

    st.markdown(
        f'<div class="total">🎉 Grand Total: ₹{grand_total:.2f}</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.info(
        "🍿 Enjoy your movie! Please arrive at the theatre "
        "15 minutes before the show."
    )

    st.caption(
        f"Booking generated on "
        f"{datetime.now().strftime('%d-%m-%Y %I:%M %p')}"
    )

