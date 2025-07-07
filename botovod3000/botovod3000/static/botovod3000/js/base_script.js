 // JavaScript для динамического дублирования содержимого (чтобы не было пустого пространства)
        document.addEventListener('DOMContentLoaded', function() {
            const runningLineContent = document.querySelector('.running-line-content');
            const content = runningLineContent.innerHTML;
            
            // Дублируем содержимое 3 раза для плавного перехода
            runningLineContent.innerHTML = content + content + content;
            
            // Опционально: можно рассчитать время анимации based on text length
            // const textLength = runningLineContent.textContent.length;
            // const duration = Math.max(10, textLength / 5);
            // runningLineContent.style.animationDuration = duration + 's';
        });