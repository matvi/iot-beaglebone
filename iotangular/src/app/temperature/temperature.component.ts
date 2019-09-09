import { Component, OnInit } from '@angular/core';
import { SocketService } from '../_sevices/socket.service';

@Component({
  selector: 'app-temperature',
  templateUrl: './temperature.component.html',
  styleUrls: ['./temperature.component.css']
})
export class TemperatureComponent implements OnInit {

  constructor(private socket: SocketService) { }

  ngOnInit() {
  }

  sendmessage(){
    this.socket.sendMessage('Hi flask');
  }

}
