module.exports = {
    content: [
        './templates/*.html',
        './templates/chunks/*.html',
        './static/js/**/*.js',
        // Add other paths to your templates and static files
    ],
    theme: {
        extend: {
          colors: {
            'purple-70%': "rgba(144, 0, 255, 0.7)",
            'black-30%': "rgba(0, 0, 0, 0.3)",
            'contact': "rgba(41, 41, 43, 0.2)",
          },
          screens: {
            '1180px': '1180px',
            '1000px': '1000px',
            '900px': '900px',
          }
        },
    },
    plugins: [],
};