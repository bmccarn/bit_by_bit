function quoteGenerator() {
    let quotes =
        [
            '"When you have a dream, you’ve got to grab it and never let go." -Carol Burnett',
            '"There is nothing impossible to they who will try." — Alexander the Great',
            '"The bad news is time flies. The good news is you’re the pilot." — Michael Altshuler',
            '"Keep your face always toward the sunshine, and shadows will fall behind you." — Walt Whitman',
            '"What lies behind you and what lies in front of you, pales in comparison to what lies inside of you." — Ralph Waldo Emerson',
            '"Belief creates the actual fact." — William James',
            '"It is during our darkest moments that we must focus to see the light." — Aristotle',
            '"Believe you can and you’re halfway there." – Theodore Roosevelt',
            '"In a gentle way, you can shake the world." — Mahatma Gandhi',
            '"Learning how to be still, to really be still and let life happen—that stillness becomes a radiance.” — Morgan Freeman'
        ]

    let randomNumber = Math.floor(Math.random() * (quotes.length));
    document.getElementById("quoteOutput").innerHTML = quotes[randomNumber];
}