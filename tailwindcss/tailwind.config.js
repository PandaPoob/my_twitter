/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["../views/*.html"],
  theme: {
    extend: {
      screens: {
        sm: "500px",
        md: "987px",
        lg: "1265px",
        xl: "1500px",
        xxl: "1800px",
      },
      fontFamily: {
        body: ['"Open Sans"'],
      },
      fontSize: {
        sm: ["0.813rem", { lineHeight: "normal" }], //13px
        md: ["0.875em", { lineHeight: "normal" }], //14px
        base: ["0.938rem", { lineHeight: "normal" }], //15px
        lg: ["1.063rem", { lineHeight: "normal" }], //17px
        xl: ["1.25rem", { lineHeight: "normal" }], //20px,
        xxl: ["1.75rem", { lineHeight: "normal" }], //32px,
      },
      colors: {
        twitterblue: "#1d9bf0",
        twittergold: "#e2b719",
        twitterborder: "#2f3336",
        twitterbuttonborder: "#536471",
        "twittergray-400": "#e7e9ea",
        "twittergray-500": "#71767b",
        "twittergray-800": "#202327",
        "twittergray-900": "#16181c",
        twitterRed: "#f4212e",
      },
      maxWidth: {
        layout: "1800px",
        feed: "600px",
        widget: "290px",
        widgetxl: "350px",
      },
      minWidth: {
        widget: "290px",
        widgetxl: "350px",
      },
      width: {
        widget: "290px",
        widgetxl: "350px",
      },
      maxHeight: {
        tweetImg: "480px",
      },
    },
  },
  plugins: [],
};
