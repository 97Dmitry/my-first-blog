<template>
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
  Информация о сайте
</button>

<!-- Modal -->
<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
     aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h2 class="modal-title text-dark " style="font-weight: 800;" id="staticBackdropLabel">Сайт PostBlog</h2>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body text-dark">
        <h4>Тестовый сайт, созданный с целью обучения программированию</h4>
        <br/>
        <p>Вся информация в постах на этом сайте взята с открытых источников</p>
        <p>Исходный код этого сайта находится на моём <a href="https://github.com/97Dmitry/">GitHub'е</a></p>
        <p>Так же для подробной информации и обратной связи создан <a
          href="https://t.me/PostBlogSite_bot">TelegramBot</a></p>
        <br/>
        <div class="progress" style="width: 450px;">
          <div class="progress-bar progress-bar-striped bg-success" role="progressbar"
               style="width: 37%" aria-valuenow="70" aria-valuemin="10" aria-valuemax="100">Сайт завершен на 37%
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Понятно</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "ModalWindow"
}
</script>