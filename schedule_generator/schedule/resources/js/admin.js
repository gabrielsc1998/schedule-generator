window.onload = () => {
    const ministry = document.getElementById('id_ministry');
    const activitiesSelector = document.getElementById('id_activities_from');
    ministry.addEventListener('change', () => {
        console.log(ministry.value);
    });
}