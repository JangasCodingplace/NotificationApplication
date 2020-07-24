class NotificationObj{
  constructor(notificationObj){
    this.notificationObj = notificationObj
  }
  creationReminder(){
    var reminder = `
      <a class="dropdown-item d-flex align-items-center" href="#">
        <div class="mr-3">
          <div class="icon-circle bg-primary">
            <i class="fas fa-file-alt text-white"></i>
          </div>
        </div>
        <div>
          <div class="small text-gray-500">
            ${this.notificationObj.creation_date}
          </div>
          ${this.notificationObj.body}
        </div>
      </a>
    `
    return reminder;
  }
  doneReminder(){
    var reminder = `
      <a class="dropdown-item d-flex align-items-center" href="#">
        <div class="mr-3">
          <div class="icon-circle bg-success">
            <i class="fas fa-donate text-white"></i>
          </div>
        </div>
        <div>
          <div class="small text-gray-500">
            ${this.notificationObj.creation_date}
          </div>
          ${this.notificationObj.body}
        </div>
      </a>
    `
    return reminder;
  }
  systemReminder(){
    var reminder = `
      <a class="dropdown-item d-flex align-items-center" href="#">
        <div class="mr-3">
          <div class="icon-circle bg-warning">
            <i class="fas fa-exclamation-triangle text-white"></i>
          </div>
        </div>
        <div>
        <div class="small text-gray-500">
          ${this.notificationObj.creation_date}
        </div>
        ${this.notificationObj.body}
        </div>
      </a>
    `
    return reminder;
  }
  drawNotification(){
    if (this.notificationObj.group === 'c') return this.creationReminder();
    if (this.notificationObj.group === 'd') return this.doneReminder();
    return this.systemReminder();
  }
}